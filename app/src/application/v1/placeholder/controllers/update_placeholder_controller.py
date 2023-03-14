from aiohttp.web_request import Request
from app.src.application.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.src.application.v1.placeholder.schemas.update import schema as update_schema
from app.src.application.v1.placeholder.adapter.update_placeholder_adapter import UpdateplaceholderAdapter
from app.src.infrastructure.v1.placeholder.services.update_placeholder_service import UpdatePlaceholderService
from app.src.infrastructure.v1.placeholder.repositories.update_placeholder_repository import UpdatePlaceholderRepository
from app.src.infrastructure.v1.placeholder.gateways.update_placeholder_gateway import UpdatePaceholderGateway
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.application.v1.placeholder.transformers.update_placeholder_transformer import UpdateplaceholderTranformer
from app.bootstrap.logger import logger


class UpdatePlaceholderController(Controller):
    """[Update placeholder controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = UpdatePlaceholderService(
            UpdatePlaceholderRepository(
                UpdatePaceholderGateway()
            ),
            PlaceholderEvent("update_placeholder_event")
        )

    @property
    def schema(self) -> dict:
        return update_schema

    @error
    @validateHeaders
    @validateParams
    @validateQuery
    @validateBody
    async def handle(self, request: Request):
        """[Update placeholder controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('UpdateplaceholderController handle')

        return self.response(
            UpdateplaceholderTranformer.transform(
                await self.__service.excute(
                    data=await UpdateplaceholderAdapter(request).adapt()
                )
            ),
            201
        )
