from aiohttp.web_request import Request
from aiohttp.web_response import Response
from app.src.application.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.src.application.v1.user.schemas.read import schema as read_schema
from app.src.application.v1.user.adapter.read_user_adapter import ReaduserAdapter
from app.src.infrastructure.v1.user.services.read_user_service import ReadUserService
from app.src.infrastructure.v1.user.repositories.read_user_repository import ReadUserRepository
from app.src.infrastructure.v1.user.events import UserEvent
from app.src.application.v1.user.transformers.read_user_transformer import ReadUserTranformer
from app.src.infrastructure.v1.user.entities import User
from app.bootstrap.logger import logger


class ReadUserController(Controller):
    """[Read user controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = ReadUserService(
            ReadUserRepository(),
            UserEvent("read_user_event")
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
        """[Read user controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('ReaduserController handle')

        entity: User = await self.__service.excute(data=await ReaduserAdapter(request).adapt())

        return self.response(
            ReadUserTranformer.transform(data=entity),
            200
        )
