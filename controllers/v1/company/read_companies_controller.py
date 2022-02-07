from aiohttp.web_request import Request
from aiohttp.web_response import Response
from controllers.v1 import Controller, error
from controllers.v1.company import read_schema
from src.services.company.read_companies_service import ReadCompaniesService
from src.repositories.company.company_repository import CompanyRepository
from src.events.company import CompanyEvent
from bootstrap.logger import logger


class ReadCompaniesController(Controller):
    """[Read company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = ReadCompaniesService(
            CompanyRepository(),
            CompanyEvent("read_companies_event")
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
            await self.__service.excute(),
            200
        )
