from aiohttp.web_request import Request
from app.http.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.http.v1.company.schemas.create import schema as create_schema
from app.http.v1.company.adapter.create_company_adapter import CreateCompanyAdapter
from app.http.v1.company.transformers.create_company_transformer import CreateCompanyTranformer
from app.src.v1.company.services.create_company_service import CreateCompanyService
from app.src.v1.company.repositories.create_company_repository import CreateCompanyRepository
from app.src.v1.company.events import CompanyEvent
from app.bootstrap.logger import logger


class CreateCompanyController(Controller):
    """[Create company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = CreateCompanyService(
            CreateCompanyRepository(),
            CompanyEvent("create_company_event")
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
        """[Create company controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('CreateCompanyController handle')

        return self.response(
            CreateCompanyTranformer.transform(
                await self.__service.excute(
                    data=await CreateCompanyAdapter(request).adapt()
                )
            ),
            201
        )
