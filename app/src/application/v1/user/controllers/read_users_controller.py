from aiohttp.web_request import Request
from aiohttp.web_response import Response
from app.src.application.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.src.application.v1.user.schemas.read_all import schema as read_all_schema
from app.src.infrastructure.v1.user.services.read_users_service import ReadUsersService
from app.src.infrastructure.v1.user.repositories.read_users_repository import ReadUsersRepository
from app.src.infrastructure.v1.user.events import UserEvent
from app.bootstrap.logger import logger
from app.src.application.v1.user.adapter.read_users_adapter import ReadUsersAdapter
from app.src.application.v1.user.transformers.read_users_transformer import ReadUsersTranformer


class ReadUsersController(Controller):
    """[Read user controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = ReadUsersService(
            ReadUsersRepository(),
            UserEvent("read_users_event")
        )

    @property
    def schema(self) -> dict:
        return read_all_schema

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

        query = await ReadUsersAdapter(request).adapt()

        return self.response(
            ReadUsersTranformer.transform(
                data=await self.__service.excute(
                    query=query
                ),
                query=query
            ),
            200
        )
