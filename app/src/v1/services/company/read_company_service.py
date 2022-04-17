from app.src.service import Service
from app.src.v1.exceptions.company.events import CompanyEventExcepion
from app.src.v1.events.company import CompanyEvent
from app.src.v1.exceptions.company.repositories import CompanyReadByIdExcepion
from app.src.v1.repositories.company.read_company_repository import ReadCompanyRepository
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
            logger.error({"error": f"ReadCompanyService ReadCompanyRepository readById: {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise Exception(e)

        try:
            # CompanyEvent("read_company_event")
            self.__event.dispatch(id=id)
        except CompanyEventExcepion as e:
            logger.error({"error": f"ReadCompanyService CompanyEvent dispatch: {e.__repr__}"})
            logger.error(traceback.format_exc())

        return response
