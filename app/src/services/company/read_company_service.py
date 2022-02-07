from app.src.services import Service
from app.src.events.company import CompanyEvent, CompanyEventExcepion
from app.src.repositories.company import CompanyReadByIdExcepion
from app.src.repositories.company.company_repository import CompanyRepository
import traceback
from app.bootstrap.logger import logger


class ReadCompanyService(Service):
    """[Read company service]

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

    async def excute(self, id: str) -> dict:
        """[Execute]

        Args:
            id (str): [id entity to read]

        Raises:
            Exception: [description]

        Returns:
            dict: [to response]
        """

        response = {}

        logger.info(f"ReadCompanyService excute id={id}")

        try:
            response = await self.__repo.readById(id=id)
        except CompanyReadByIdExcepion as e:
            logger.error({"error": f"ReadCompanyService CompanyRepository readById: {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise Exception(e)

        try:
            # CompanyEvent("read_company_event")
            self.__event.dispatch(id=id)
        except CompanyEventExcepion as e:
            logger.error({"error": f"ReadCompanyService CompanyEvent dispatch: {e.__repr__}"})
            logger.error(traceback.format_exc())

        return response
