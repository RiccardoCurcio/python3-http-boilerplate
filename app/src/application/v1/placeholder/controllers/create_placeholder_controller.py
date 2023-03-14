from aiohttp.web_request import Request
from app.src.application.abc.controllers import (
    Controller,
    error,
    validateHeaders,
    validateParams,
    validateQuery,
    validateBody,
)
from app.src.application.v1.placeholder.schemas.create import schema as create_schema
from app.src.application.v1.placeholder.adapter.create_placeholder_adapter import (
    CreateplaceholderAdapter,
)
from app.src.application.v1.placeholder.transformers.create_placeholder_transformer import (
    CreateplaceholderTranformer,
)
from app.src.infrastructure.v1.placeholder.services.create_placeholder_service import (
    CreatePlaceholderService,
)
from app.src.infrastructure.v1.placeholder.repositories.create_placeholder_repository import (
    CreatePlaceholderRepository,
)
from app.src.infrastructure.v1.placeholder.gateways.create_placeholder_gateway import CreatePaceholderGateway
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.bootstrap.logger import logger


class CreatePlaceholderController(Controller):
    """[Create placeholder controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = CreatePlaceholderService(
            CreatePlaceholderRepository(
                CreatePaceholderGateway()
            ), PlaceholderEvent("create_placeholder_event")
        )

    @property
    def schema(self) -> dict:
        return create_schema

    @error
    @validateHeaders
    @validateParams
    @validateQuery
    @validateBody
    async def handle(self, request: Request):
        """[Create placeholder controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info("CreateplaceholderController handle")

        entity: Placeholder = await self.__service.excute(
            data=await CreateplaceholderAdapter(request).adapt()
        )

        return self.response(CreateplaceholderTranformer.transform(data=entity), 201)
