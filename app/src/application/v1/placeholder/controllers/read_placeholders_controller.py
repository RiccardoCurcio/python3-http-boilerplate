from aiohttp.web_request import Request
from aiohttp.web_response import Response
from app.src.application.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.src.application.v1.placeholder.schemas.read_all import schema as read_all_schema
from app.src.infrastructure.v1.placeholder.services.read_placeholders_service import ReadPlaceholdersService
from app.src.infrastructure.v1.placeholder.repositories.read_placeholders_repository import ReadPlaceholdersRepository
from app.src.infrastructure.v1.placeholder.gateways.read_placeholders_gateway import ReadPaceholdersGateway
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.bootstrap.logger import logger
from app.src.application.v1.placeholder.adapter.read_placeholders_adapter import ReadPlaceholdersAdapter
from app.src.application.v1.placeholder.transformers.read_placeholders_transformer import ReadPlaceholdersTranformer


class ReadPlaceholdersController(Controller):
    """[Read placeholder controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = ReadPlaceholdersService(
            ReadPlaceholdersRepository(
                ReadPaceholdersGateway()
            ),
            PlaceholderEvent("read_placeholders_event")
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
        """[Read placeholder controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('ReadplaceholderController handle')

        query = await ReadPlaceholdersAdapter(request).adapt()

        return self.response(
            ReadPlaceholdersTranformer.transform(
                data=await self.__service.excute(
                    query=query
                ),
                query=query
            ),
            200
        )
