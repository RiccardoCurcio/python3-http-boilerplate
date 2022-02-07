from app.src.services import Service
import traceback
from app.bootstrap.logger import logger
from app.src.events.company import CompanyEvent, CompanyEventExcepion
from app.src.repositories.company import CompanyCreateExcepion
from app.src.repositories.company.company_repository import CompanyRepository


class CreateCompanyService(Service):
    """[Create company service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(self, repository: CompanyRepository, event: CompanyEvent) -> None:
        """[summary]

        Args:
            repository (CompanyRepository): [description]
            event (CompanyEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: dict) -> dict:
        """[Create company service]

        Args:
            id (str): [id entity to create]
            data (dict): [data to create]

        Raises:
            Exception: []

        Returns:
            dict: [to reponse]
        """
        response = {}
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
