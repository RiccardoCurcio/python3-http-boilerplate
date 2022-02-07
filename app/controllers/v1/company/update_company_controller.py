from aiohttp.web_request import Request
from controllers.v1 import Controller, error, validate
from controllers.v1.company import update_schema
from src.services.company.update_company_service import UpdateCompanyService
from src.repositories.company.company_repository import CompanyRepository
from src.events.company import CompanyEvent
from bootstrap.logger import logger


class UpdateCompanyController(Controller):
    """[Update company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = UpdateCompanyService(
            CompanyRepository(),
            CompanyEvent("update_company_event")
        )

    @property
    def schema(self) -> dict:
        return update_schema

    @error
    @validate
    async def handle(self, request: Request):
        """[Update company controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('UpdateCompanyController handle')
        data = await request.json()

        return self.response(
            await self.__service.excute(
                id=request.match_info.get('entity_id', None),
                data=data
            ),
            201
        )
