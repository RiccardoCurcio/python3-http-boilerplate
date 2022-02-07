from aiohttp.web_request import Request
from aiohttp.web_response import Response
from app.controllers.v1 import Controller, error
from app.controllers.v1.company import read_schema
from app.src.services.company.read_company_service import ReadCompanyService
from app.src.repositories.company.company_repository import CompanyRepository
from app.src.events.company import CompanyEvent
from app.bootstrap.logger import logger


class ReadCompanyController(Controller):
    """[Read company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = ReadCompanyService(
            CompanyRepository(),
            CompanyEvent("read_company_event")
        )

    @property
    def schema(self) -> dict:
        return read_schema

    @error
    async def handle(self, request: Request) -> Response:
        """[Read company controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('ReadCompanyController handle')

        return self.response(
            await self.__service.excute(
                id=request.match_info.get('entity_id', None)
            ),
            200
        )
