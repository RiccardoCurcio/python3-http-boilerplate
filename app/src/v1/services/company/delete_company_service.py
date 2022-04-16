from app.src.service import Service
import traceback
from app.bootstrap.logger import logger
from app.src.v1.exceptions.company.events import CompanyEventExcepion
from app.src.v1.events.company import CompanyEvent
from app.src.v1.exceptions.company.repositories import CompanyDeleteExcepion
from app.src.v1.repositories.company.company_repository import CompanyRepository


class DeleteCompanyService(Service):
    """[Delete company service]

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

    async def excute(self, id: str) -> dict:
        """[Delete company service]

        Args:
            id (str): [id entity to delete]

        Raises:
            Exception: []

        Returns:
            dict: [to reponse]
        """
        response = {}
        logger.info(f"DeleteCompanyService excute id={id}")

        try:
            response = await self.__repo.delete(id=id)
        except CompanyDeleteExcepion as e:
            logger.error({"error": f"DeleteCompanyService CompanyRepository delete: {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise Exception(e)
        try:
            self.__event.dispatch(id=id)
        except CompanyEventExcepion as e:
            logger.error({"error": f"DeleteCompanyService CompanyEvent dispatch: {e.__repr__}"})
            logger.error(traceback.format_exc())

        return response
