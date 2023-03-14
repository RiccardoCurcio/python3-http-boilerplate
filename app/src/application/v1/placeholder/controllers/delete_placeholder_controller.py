from aiohttp.web_request import Request
from app.src.application.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.src.application.v1.placeholder.schemas.delete import schema as delete_schema
from app.src.application.v1.placeholder.adapter.delete_placeholder_adapter import DeleteplaceholderAdapter
from app.src.infrastructure.v1.placeholder.services.delete_placeholder_service import DeletePlaceholderService
from app.src.infrastructure.v1.placeholder.repositories.delete_placeholder_repository import DeletePlaceholderRepository
from app.src.infrastructure.v1.placeholder.gateways.delete_placeholder_gateway import DeletePaceholderGateway
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.application.v1.placeholder.transformers.delete_placeholder_transformer import DeleteplaceholderTranformer
from app.bootstrap.logger import logger


class DeletePlaceholderController(Controller):
    """[Delete placeholder controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = DeletePlaceholderService(
            DeletePlaceholderRepository(
                DeletePaceholderGateway()
            ),
            PlaceholderEvent("delete_placeholder_event")
        )

    @property
    def schema(self) -> dict:
        return delete_schema

    @error
    @validateHeaders
    @validateParams
    @validateQuery
    @validateBody
    async def handle(self, request: Request):
        """[Delete placeholder controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('DeletePlaceholderController handle')

        return self.response(
            DeleteplaceholderTranformer.transform(
                await self.__service.excute(
                    data=await DeleteplaceholderAdapter(request).adapt()
                )
            ),
            200
        )
