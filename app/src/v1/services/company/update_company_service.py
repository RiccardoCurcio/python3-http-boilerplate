from app.src.service import Service
import traceback
from app.bootstrap.logger import logger
from app.src.v1.entities.company import Company
from app.src.v1.exceptions.company.events import CompanyEventExcepion
from app.src.v1.events.company import CompanyEvent
from app.src.v1.exceptions.company.repositories import CompanyUpdateExcepion
from app.src.v1.repositories.company.update_company_repository import UpdateCompanyRepository


class UpdateCompanyService(Service):
    """[Update company service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(self, repository: UpdateCompanyRepository, event: CompanyEvent) -> None:
        """[summary]

        Args:
            repository (UpdateCompanyRepository): [description]
            event (CompanyEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: Company) -> dict:
        """[Update company service]

        Args:
            id (str): [id entity to update]
            data (dict): [data to update]

        Raises:
            Exception: []

        Returns:
            dict: [to reponse]
        """
        response = {}
        logger.info(f"UpdateCompanyService excute id={data.id}")

        try:
            response = await self.__repo.update(data=data)
        except CompanyUpdateExcepion as e:
            logger.error({"error": f"UpdateCompanyService UpdateCompanyRepository update: {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise Exception(e)
        try:
            self.__event.dispatch(data=data)
        except CompanyEventExcepion as e:
            logger.error({"error": f"UpdateCompanyService CompanyEvent dispatch: {e.__repr__}"})
            logger.error(traceback.format_exc())

        return response
