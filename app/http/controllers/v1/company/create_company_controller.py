from aiohttp.web_request import Request
from app.http.controllers import Controller, error, validate
from app.http.controllers.v1.company import create_schema
from app.http.adapter.v1.company.create_company_adapter import CreateCompanyAdapter
from app.src.v1.services.company.create_company_service import CreateCompanyService
from app.src.v1.repositories.company.company_repository import CompanyRepository
from app.src.v1.events.company import CompanyEvent
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

        return self.response(
            (
                await self.__service.excute(
                    data=await CreateCompanyAdapter(request).adapt()
                )
            ).to_dict(),
            201
        )
