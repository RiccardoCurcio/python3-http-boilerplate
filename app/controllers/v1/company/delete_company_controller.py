from aiohttp.web_request import Request
from app.controllers.v1 import Controller, error
from app.controllers.v1.company import delete_schema
from app.src.services.company.delete_company_service import DeleteCompanyService
from app.src.repositories.company.company_repository import CompanyRepository
from app.src.events.company import CompanyEvent
from app.bootstrap.logger import logger


class DeleteCompanyController(Controller):
    """[Delete company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = DeleteCompanyService(
            CompanyRepository(),
            CompanyEvent("delete_company_event")
        )

    @property
    def schema(self) -> dict:
        return delete_schema

    @error
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
            201
        )
