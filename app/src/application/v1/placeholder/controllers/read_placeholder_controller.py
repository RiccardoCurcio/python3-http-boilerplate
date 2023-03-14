from aiohttp.web_request import Request
from aiohttp.web_response import Response
from app.src.application.abc.controllers import (
    Controller,
    error,
    validateHeaders,
    validateParams,
    validateQuery,
    validateBody,
)
from app.src.application.v1.placeholder.schemas.read import schema as read_schema
from app.src.application.v1.placeholder.adapter.read_placeholder_adapter import (
    ReadplaceholderAdapter,
)
from app.src.infrastructure.v1.placeholder.services.read_placeholder_service import (
    ReadPlaceholderService,
)
from app.src.infrastructure.v1.placeholder.repositories.read_placeholder_repository import (
    ReadPlaceholderRepository,
)
from app.src.infrastructure.v1.placeholder.gateways.read_placeholder_gateway import ReadPaceholderGateway
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.application.v1.placeholder.transformers.read_placeholder_transformer import (
    ReadPlaceholderTranformer,
)
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.bootstrap.logger import logger


class ReadPlaceholderController(Controller):
    """[Read placeholder controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = ReadPlaceholderService(
            ReadPlaceholderRepository(
                ReadPaceholderGateway()
            ), PlaceholderEvent("read_placeholder_event")
        )

    @property
    def schema(self) -> dict:
        return read_schema

    @error
    @validateHeaders
    @validateParams
    @validateQuery
    @validateBody
    async def handle(self, request: Request) -> Response:
        """[Read placeholder controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info("ReadplaceholderController handle")

        entity: Placeholder = await self.__service.excute(
            data=await ReadplaceholderAdapter(request).adapt()
        )

        return self.response(ReadPlaceholderTranformer.transform(data=entity), 200)
