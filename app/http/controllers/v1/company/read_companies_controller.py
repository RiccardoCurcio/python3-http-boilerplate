from aiohttp.web_request import Request
from aiohttp.web_response import Response
from app.http.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.http.controllers.v1.company import read_all_schema
from app.src.v1.services.company.read_companies_service import ReadCompaniesService
from app.src.v1.repositories.company.read_companies_repository import ReadCompaniesRepository
from app.src.v1.events.company import CompanyEvent
from app.bootstrap.logger import logger
from app.http.adapter.v1.company.read_companies_adapter import ReadCompaniesAdapter
from app.http.transformers.v1.company.read_companies_transformer import ReadCompaniesTranformer


class ReadCompaniesController(Controller):
    """[Read company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = ReadCompaniesService(
            ReadCompaniesRepository(),
            CompanyEvent("read_companies_event")
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
        """[Read company controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('ReadCompanyController handle')

        query = await ReadCompaniesAdapter(request).adapt()

        return self.response(
            ReadCompaniesTranformer.transform(
                data=await self.__service.excute(
                    query=query
                ),
                query=query
            ),
            200
        )
