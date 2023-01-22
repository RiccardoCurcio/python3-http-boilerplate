import json
import os
import traceback
from typing import Any
from abc import ABC, abstractmethod
from aiohttp.web_exceptions import HTTPBadRequest, HTTPError
from app.src.domain.valuesobjects import ValueObjectExcepion
from aiohttp.web_request import Request
from aiohttp import web
from jsonschema import validate as validate_json
from jsonschema.exceptions import ValidationError
from app.corss_origin import corss_headers
from app.bootstrap.logger import logger


def validateHeaders(handle):
    """_summary_

    Args:
        handle (_type_): _description_

    Raises:
        HTTPBadRequest: _description_

    Returns:
        _type_: _description_
    """
    @error
    async def wrapper(controller, request: Request):
        headers = dict(
            map(
                lambda item: item,
                request.raw_headers
            )
        )

        headers = {y.decode('ascii'): headers.get(y).decode('ascii')
                   for y in headers.keys()}

        try:
            validate_json(
                instance=headers,
                schema=controller.schema.get("headers", None)
            )
        except ValidationError as e:
            logger.error(e)
            raise HTTPBadRequest(reason=e.message)

        return await handle(controller, request)

    return wrapper


def validateParams(handle):
    """_summary_

    Args:
        handle (_type_): _description_

    Raises:
        HTTPBadRequest: _description_

    Returns:
        _type_: _description_
    """
    @error
    async def wrapper(controller, request: Request):
        try:
            validate_json(
                instance=dict(request.match_info),
                schema=controller.schema.get("params", None)
            )
        except ValidationError as e:
            logger.error(e)
            raise HTTPBadRequest(reason=e.message)

        return await handle(controller, request)

    return wrapper


def validateQuery(handle):
    """_summary_

    Args:
        handle (_type_): _description_

    Raises:
        HTTPBadRequest: _description_

    Returns:
        _type_: _description_
    """
    @error
    async def wrapper(controller, request: Request):
        try:
            validate_json(
                instance=dict(request.rel_url.query),
                schema=controller.schema.get("query", None)
            )
        except ValidationError as e:
            logger.error(e)
            raise HTTPBadRequest(reason=e.message)

        return await handle(controller, request)

    return wrapper


def validateBody(handle):
    """_summary_

    Args:
        handle (_type_): _description_

    Raises:
        HTTPBadRequest: _description_

    Returns:
        _type_: _description_
    """
    @error
    async def wrapper(controller, request: Request):
        try:
            validate_json(
                instance=await controller.to_json(request),
                schema=controller.schema.get("body", None)
            )
        except ValidationError as e:
            logger.error(e)
            raise HTTPBadRequest(reason=e.message)

        return await handle(controller, request)

    return wrapper


def error(handle):
    """_summary_

    Args:
        handle (_type_): _description_
    """
    async def wrapper(controller, request: Request):
        try:
            return await handle(controller, request)
        except HTTPError as e:
            return await controller.error(
                request,
                e.reason,
                "HTTP Error",
                e.status
            )
        except ValueObjectExcepion as e:
            if os.getenv("ENV") == "local":
                logger.error(traceback.format_exc())
            return await controller.error(request=request, detail=str(e), title="ValueObject rules Exception", status=400)
        except Exception as e:
            if os.getenv("ENV") == "local":
                logger.error(traceback.format_exc())
            return await controller.error(request, str(e))

    return wrapper


class Controller(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_

    Returns:
        _type_: _description_
    """
    @abstractmethod
    @error
    async def handle(self, request: Request):
        """_summary_

        Args:
            request (Request): _description_
        """
        pass

    @property
    @abstractmethod
    def schema(self) -> dict:
        """_summary_

        Returns:
            dict: _description_
        """
        pass

    @staticmethod
    async def to_json(request: Request) -> dict:
        """_summary_

        Args:
            request (Request): _description_

        Returns:
            dict: _description_
        """
        return await request.json() if request.body_exists else {}

    async def error(self,
                    request: Request,
                    detail: str = "There was an error during the execution",
                    title: str = "Internal server error",
                    status: int = 500,
                    ):
        """_summary_

        Args:
            request (Request): _description_
            detail (str, optional): _description_. Defaults to "There was an error during the execution".
            title (str, optional): _description_. Defaults to "Internal server error".
            status (int, optional): _description_. Defaults to 500.

        Returns:
            _type_: _description_
        """
        method = request.method
        url = request.url
        text = f"{json.loads(await request.text() or '{}')}"
        logger.error(
            f"{title}: {detail} | {method} {url} {text}"
        )
        return self.response(
            data={
                "status": status,
                "title": title,
                "detail": detail
            },
            status=status
        )

    @staticmethod
    def response(data: Any = None, status: int = 200, customHeader: dict = {}):
        """_summary_

        Args:
            data (Any, optional): _description_. Defaults to None.
            status (int, optional): _description_. Defaults to 200.
            customHeader (dict, optional): _description_. Defaults to {}.

        Returns:
            _type_: _description_
        """
        server = {"Server": os.getenv("SERVICE_NAME", "PY3-http-boilerplate")}
        __corss_headers = corss_headers if os.getenv(
            "CORSS_ORIGIN_RESOLVE", False) in ("1", "True", "true", True) else {}
        data_response = {}
        if 200 <= status < 300:
            data_response.update(success=True)
            data_response.update(data=data)
        else:
            data_response.update(success=False)
            data_response.update(error=data)

        return web.json_response(
            data=data_response,
            status=status,
            content_type="application/vnd.api+json",
            headers={**__corss_headers, **server, **customHeader}
        )
