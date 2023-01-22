from app.src.domain.abc.service import Service
from app.src.infrastructure.v1.company.queries import Company
from app.src.infrastructure.v1.company.exceptions.events import CompanyEventExcepion
from app.src.infrastructure.v1.company.events import CompanyEvent
from app.src.infrastructure.v1.company.exceptions.repositories import CompaniesReadExcepion
from app.src.infrastructure.v1.company.repositories.read_companies_repository import ReadCompaniesRepository
import traceback
from app.bootstrap.logger import logger


class ReadCompaniesService(Service):
    """[Read companies service]

    Args:
        Service ([Service]): [ADS service]
    """

    def __init__(self, repository: ReadCompaniesRepository, event: CompanyEvent) -> None:
        """[summary]

        Args:
            repository (ReadCompaniesRepository): [description]
            event (CompanyEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, query: Company) -> dict:
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
            response = await self.__repo.read(query)
        except CompaniesReadExcepion as e:
            logger.error({"error": f"ReadCompaniesService ReadCompaniesRepository read all: {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise Exception(e)

        try:
            self.__event.dispatch()
        except CompanyEventExcepion as e:
            logger.error({"error": f"ReadCompaniesService CompanyEvent dispatch: {e.__repr__}"})
            logger.error(traceback.format_exc())

        return response
