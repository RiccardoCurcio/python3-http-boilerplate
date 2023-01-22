from typing import Union
from app.src.domain.abc.service import Service
from app.src.infrastructure.v1.company.exceptions.events import CompanyEventExcepion
from app.src.infrastructure.v1.company.events import CompanyEvent
from app.src.infrastructure.v1.company.entities import Company
from app.src.infrastructure.v1.company.exceptions.repositories import CompanyReadByIdExcepion
from app.src.infrastructure.v1.company.repositories.read_company_repository import ReadCompanyRepository
import traceback
from app.bootstrap.logger import logger


class ReadCompanyService(Service):
    """[Read company service]

    Args:
        Service ([Service]): [ADS service]
    """

    def __init__(self, repository: ReadCompanyRepository, event: CompanyEvent) -> None:
        """[summary]

        Args:
            repository (ReadCompanyRepository): [description]
            event (CompanyEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: Company) -> Union[Company, None]:
        """[Execute]

        Args:
            id (str): [id entity to read]

        Raises:
            Exception: [description]

        Returns:
            dict: [to response]
        """

        response = {}

        logger.info(f"ReadCompanyService excute id={data.id}")

        try:
            response = await self.__repo.readById(data=data)
        except CompanyReadByIdExcepion as e:
            logger.error({"error": f"ReadCompanyService ReadCompanyRepository readById: {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise Exception(e)

        try:
            self.__event.dispatch(data=data)
        except CompanyEventExcepion as e:
            logger.error({"error": f"ReadCompanyService CompanyEvent dispatch: {e.__repr__}"})
            logger.error(traceback.format_exc())

        return response
