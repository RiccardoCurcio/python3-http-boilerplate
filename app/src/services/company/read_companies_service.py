from app.src.services import Service
from app.src.events.company import CompanyEvent, CompanyEventExcepion
from app.src.repositories.company import CompaniesReadExcepion
from app.src.repositories.company.company_repository import CompanyRepository
import traceback
from app.bootstrap.logger import logger


class ReadCompaniesService(Service):
    """[Read companies service]

    Args:
        Service ([Service]): [ADS service]
    """

    def __init__(self, repository: CompanyRepository, event: CompanyEvent) -> None:
        """[summary]

        Args:
            repository (CompanyRepository): [description]
            event (CompanyEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self) -> dict:
        """[Execute]

        Args:
            id (str): [id entity to read]

        Raises:
            Exception: [description]

        Returns:
            dict: [to response]
        """

        response = {}

        logger.info("ReadCompaniesService excute ")

        try:
            response = await self.__repo.read()
        except CompaniesReadExcepion as e:
            logger.error({"error": f"ReadCompaniesService CompanyRepository read all: {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise Exception(e)

        try:
            self.__event.dispatch()
        except CompanyEventExcepion as e:
            logger.error({"error": f"ReadCompaniesService CompanyEvent dispatch: {e.__repr__}"})
            logger.error(traceback.format_exc())

        return response
