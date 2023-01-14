from aiohttp.web_request import Request
from aiohttp.web_response import Response
from app.http.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.http.v1.company.schemas.read_all import schema as read_all_schema
from app.src.v1.company.services.read_companies_service import ReadCompaniesService
from app.src.v1.company.repositories.read_companies_repository import ReadCompaniesRepository
from app.src.v1.company.events import CompanyEvent
from app.bootstrap.logger import logger
from app.http.v1.company.adapter.read_companies_adapter import ReadCompaniesAdapter
from app.http.v1.company.transformers.read_companies_transformer import ReadCompaniesTranformer


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
