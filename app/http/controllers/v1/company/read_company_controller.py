from aiohttp.web_request import Request
from aiohttp.web_response import Response
from app.http.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.http.controllers.v1.company import read_schema
from app.http.adapter.v1.company.read_company_adapter import ReadCompanyAdapter
from app.src.v1.services.company.read_company_service import ReadCompanyService
from app.src.v1.repositories.company.read_company_repository import ReadCompanyRepository
from app.src.v1.events.company import CompanyEvent
from app.http.transformers.v1.company.read_company_transformer import ReadCompanyTranformer
from app.bootstrap.logger import logger


class ReadCompanyController(Controller):
    """[Read company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """

    def __init__(self) -> None:
        self.__service = ReadCompanyService(
            ReadCompanyRepository(),
            CompanyEvent("read_company_event")
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
        """[Read company controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('ReadCompanyController handle')

        return self.response(
            ReadCompanyTranformer.transform(
                await self.__service.excute(
                    data=await ReadCompanyAdapter(request).adapt()
                )
            ),
            200
        )
