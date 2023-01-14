from aiohttp.web_request import Request
from app.http.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.http.v1.company.schemas.update import schema as update_schema
from app.http.v1.company.adapter.update_company_adapter import UpdateCompanyAdapter
from app.src.v1.company.services.update_company_service import UpdateCompanyService
from app.src.v1.company.repositories.update_company_repository import UpdateCompanyRepository
from app.src.v1.company.events import CompanyEvent
from app.http.v1.company.transformers.update_company_transformer import UpdateCompanyTranformer
from app.bootstrap.logger import logger


class UpdateCompanyController(Controller):
    """[Update company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = UpdateCompanyService(
            UpdateCompanyRepository(),
            CompanyEvent("update_company_event")
        )

    @property
    def schema(self) -> dict:
        return update_schema

    @error
    @validateHeaders
    @validateParams
    @validateQuery
    @validateBody
    async def handle(self, request: Request):
        """[Update company controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('UpdateCompanyController handle')

        return self.response(
            UpdateCompanyTranformer.transform(
                await self.__service.excute(
                    data=await UpdateCompanyAdapter(request).adapt()
                )
            ),
            201
        )
