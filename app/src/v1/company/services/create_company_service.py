from typing import Union
from app.src.abc.service import Service
import traceback
from app.bootstrap.logger import logger
from app.src.v1.company.entities import Company
from app.src.v1.company.exceptions.events import CompanyEventExcepion
from app.src.v1.company.events import CompanyEvent
from app.src.v1.company.exceptions.repositories import CompanyCreateExcepion
from app.src.v1.company.repositories.create_company_repository import CreateCompanyRepository


class CreateCompanyService(Service):
    """[Create company service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(self, repository: CreateCompanyRepository, event: CompanyEvent) -> None:
        """[summary]

        Args:
            repository (CreateCompanyRepository): [description]
            event (CompanyEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: Company) -> Union[Company, None]:
        """_summary_

        Args:
            data (Company): _description_

        Raises:
            Exception: _description_

        Returns:
            Union[Company, None]: _description_
        """
        response: Union[Company, None] = None
        logger.info("CreateCompanyService excute")

        try:
            response = await self.__repo.create(data=data)
        except CompanyCreateExcepion as e:
            logger.error({"error": f"CreateCompanyService CompanyRepository create: {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise Exception(e)
        try:
            self.__event.dispatch(data=data)
        except CompanyEventExcepion as e:
            logger.error({"error": f"CreateCompanyService CompanyEvent dispatch: {e.__repr__}"})
            logger.error(traceback.format_exc())

        return response
