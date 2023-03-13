from aiohttp.web_request import Request
from app.src.application.abc.controllers import (
    Controller,
    error,
    validateHeaders,
    validateParams,
    validateQuery,
    validateBody,
)
from app.src.application.v1.user.schemas.create import schema as create_schema
from app.src.application.v1.user.adapter.create_user_adapter import (
    CreateuserAdapter,
)
from app.src.application.v1.user.transformers.create_user_transformer import (
    CreateuserTranformer,
)
from app.src.infrastructure.v1.user.services.create_user_service import (
    CreateUserService,
)
from app.src.infrastructure.v1.user.repositories.create_user_repository import (
    CreateUserRepository,
)
from app.src.infrastructure.v1.user.events import UserEvent
from app.src.infrastructure.v1.user.entities import User
from app.bootstrap.logger import logger


class CreateUserController(Controller):
    """[Create user controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = CreateUserService(
            CreateUserRepository(), UserEvent("create_user_event")
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
        """[Create user controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info("CreateuserController handle")

        entity: User = await self.__service.excute(
            data=await CreateuserAdapter(request).adapt()
        )

        return self.response(CreateuserTranformer.transform(data=entity), 201)
