from aiohttp.web_request import Request
from app.controllers.v1 import Controller, error, validate
from app.controllers.v1.company import create_schema
from app.src.services.company.create_company_service import CreateCompanyService
from app.src.repositories.company.company_repository import CompanyRepository
from app.src.events.company import CompanyEvent
from app.bootstrap.logger import logger


class CreateCompanyController(Controller):
    """[Create company controller]

    Args:
        Controller ([Object]): [ABS controller]
    """
    def __init__(self) -> None:
        self.__service = CreateCompanyService(
            CompanyRepository(),
            CompanyEvent("create_company_event")
        )

    @property
    def schema(self) -> dict:
        return create_schema

    @error
    @validate
    async def handle(self, request: Request):
        """[Create company controller Handler]

        Args:
            request (Request): [http request from aiohttp]

        Returns:
            [Response]: [http response]
        """

        logger.info('CreateCompanyController handle')
        data = await request.json()

        return self.response(
            await self.__service.excute(data=data),
            201
        )
