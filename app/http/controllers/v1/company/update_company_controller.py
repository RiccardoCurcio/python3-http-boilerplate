from aiohttp.web_request import Request
from app.http.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.http.controllers.v1.company import update_schema
from app.http.adapter.v1.company.update_company_adapter import UpdateCompanyAdapter
from app.src.v1.services.company.update_company_service import UpdateCompanyService
from app.src.v1.repositories.company.update_company_repository import UpdateCompanyRepository
from app.src.v1.events.company import CompanyEvent
from app.http.transformers.v1.company.update_company_transformer import UpdateCompanyTranformer
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
