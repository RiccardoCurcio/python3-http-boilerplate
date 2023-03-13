from aiohttp.web_request import Request
from app.src.application.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.src.application.v1.user.schemas.update import schema as update_schema
from app.src.application.v1.user.adapter.update_user_adapter import UpdateuserAdapter
from app.src.infrastructure.v1.user.services.update_user_service import UpdateUserService
from app.src.infrastructure.v1.user.repositories.update_user_repository import UpdateUserRepository
from app.src.infrastructure.v1.user.events import UserEvent
from app.src.application.v1.user.transformers.update_user_transformer import UpdateuserTranformer
from app.bootstrap.logger import logger


class UpdateUserController(Controller):
    """[Update user controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = UpdateUserService(
            UpdateUserRepository(),
            UserEvent("update_user_event")
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
        """[Update user controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('UpdateuserController handle')

        return self.response(
            UpdateuserTranformer.transform(
                await self.__service.excute(
                    data=await UpdateuserAdapter(request).adapt()
                )
            ),
            201
        )
