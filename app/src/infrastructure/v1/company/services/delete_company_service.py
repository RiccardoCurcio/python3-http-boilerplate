from app.src.domain.abc.service import Service
import traceback
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.company.exceptions.events import CompanyEventExcepion
from app.src.infrastructure.v1.company.events import CompanyEvent
from app.src.infrastructure.v1.company.exceptions.repositories import CompanyDeleteExcepion
from app.src.infrastructure.v1.company.repositories.delete_company_repository import DeleteCompanyRepository
from app.src.infrastructure.v1.company.entities import Company


class DeleteCompanyService(Service):
    """[Delete company service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(self, repository: DeleteCompanyRepository, event: CompanyEvent) -> None:
        """[summary]

        Args:
            repository (DeleteCompanyRepository): [description]
            event (CompanyEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: Company) -> dict:
        """[Delete company service]

        Args:
            id (str): [id entity to delete]

        Raises:
            Exception: []

        Returns:
            dict: [to reponse]
        """
        response = {}
        logger.info(f"DeleteCompanyService excute id={data.id}")

        try:
            response = await self.__repo.delete(data=data)
        except CompanyDeleteExcepion as e:
            logger.error({"error": f"DeleteCompanyService DeleteCompanyRepository delete: {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise Exception(e)
        try:
            self.__event.dispatch(data=data)
        except CompanyEventExcepion as e:
            logger.error({"error": f"DeleteCompanyService CompanyEvent dispatch: {e.__repr__}"})
            logger.error(traceback.format_exc())

        return response