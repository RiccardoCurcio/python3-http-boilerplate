import json
import os
import traceback
from typing import Any
from abc import ABC, abstractmethod
from aiohttp.web_exceptions import HTTPBadRequest, HTTPError
from aiohttp.web_request import Request
from aiohttp import web
from jsonschema import validate as validate_json
from jsonschema.exceptions import ValidationError
from app.corss_origin import corss_headers
from app.bootstrap.logger import logger


def validate(handle):
    @error
    async def wrapper(controller, request: Request):
        if controller.schema is None:
            body = await controller.to_json(request)
            if not body:
                return await handle(controller, request)
            raise HTTPBadRequest()

        if request.content_type != "application/json":
            raise HTTPBadRequest()
        try:
            validate_json(
                instance=await controller.to_json(request),
                schema=controller.schema
            )
        except ValidationError as e:
            logger.error(e)
            raise HTTPBadRequest()

        return await handle(controller, request)

    return wrapper


def error(handle):
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
        except Exception as e:
            if os.getenv("ENV") == "local":
                logger.error(traceback.format_exc())
            return await controller.error(request, str(e))

    return wrapper


class Controller(ABC):
    @abstractmethod
    @error
    async def handle(self, request: Request):
        pass

    @property
    @abstractmethod
    def schema(self) -> dict:
        pass

    @staticmethod
    async def to_json(request: Request) -> dict:
        return await request.json() if request.body_exists else {}

    async def error(self,
                    request: Request,
                    detail: str = "There was an error during the execution",
                    title: str = "Internal server error",
                    status: int = 500,
                    ):
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
        server = {"Server": os.getenv("SERVICE_NAME", "PY3-http-boilerplate")}
        __corss_headers = corss_headers if os.getenv("CORSS_ORIGIN_RESOLVE", False) in ("1", "True", "true", True) else {}
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
