from aiohttp.web_request import Request
from app.http.controllers import Controller, error, validateHeaders, validateParams, validateQuery, validateBody
from app.http.controllers.v1.company import delete_schema
from app.src.v1.services.company.delete_company_service import DeleteCompanyService
from app.src.v1.repositories.company.delete_company_repository import DeleteCompanyRepository
from app.src.v1.events.company import CompanyEvent
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
            await self.__service.excute(id=request.match_info.get('entity_id', None)),
            200
        )
