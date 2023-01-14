from aiohttp.web_request import Request
from app.http.abc.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.http.v1.company.schemas.delete import schema as delete_schema
from app.http.v1.company.adapter.delete_company_adapter import DeleteCompanyAdapter
from app.src.v1.company.services.delete_company_service import DeleteCompanyService
from app.src.v1.company.repositories.delete_company_repository import DeleteCompanyRepository
from app.src.v1.company.events import CompanyEvent
from app.http.v1.company.transformers.delete_company_transformer import DeleteCompanyTranformer
from app.bootstrap.logger import logger


class DeleteCompanyController(Controller):
    """[Delete company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = DeleteCompanyService(
            DeleteCompanyRepository(),
            CompanyEvent("delete_company_event")
        )

    @property
    def schema(self) -> dict:
        return delete_schema

    @error
    @validateHeaders
    @validateParams
    @validateQuery
    @validateBody
    async def handle(self, request: Request):
        """[Delete company controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('DeleteCompanyController handle')

        return self.response(
            DeleteCompanyTranformer.transform(
                await self.__service.excute(
                    data=await DeleteCompanyAdapter(request).adapt()
                )
            ),
            200
        )
