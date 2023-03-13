from aiohttp.web_request import Request
from app.src.application.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.src.application.v1.user.schemas.delete import schema as delete_schema
from app.src.application.v1.user.adapter.delete_user_adapter import DeleteuserAdapter
from app.src.infrastructure.v1.user.services.delete_user_service import DeleteUserService
from app.src.infrastructure.v1.user.repositories.delete_user_repository import DeleteUserRepository
from app.src.infrastructure.v1.user.events import UserEvent
from app.src.application.v1.user.transformers.delete_user_transformer import DeleteuserTranformer
from app.bootstrap.logger import logger


class DeleteUserController(Controller):
    """[Delete user controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = DeleteUserService(
            DeleteUserRepository(),
            UserEvent("delete_user_event")
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
        """[Delete user controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('DeleteUserController handle')

        return self.response(
            DeleteuserTranformer.transform(
                await self.__service.excute(
                    data=await DeleteuserAdapter(request).adapt()
                )
            ),
            200
        )
