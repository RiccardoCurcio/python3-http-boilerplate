from src.repositories import Repository
from src.repositories.company import CompanyUpdateExcepion, CompanyReadByIdExcepion, CompaniesReadExcepion, CompanyCreateExcepion
import traceback
from bootstrap.logger import logger


class CompanyRepository(Repository):
    async def create(self, data: dict):
        """[summary]

        Args:
            data (dict): [description]

        Raises:
            CompanyCreateExcepion: [description]

        Returns:
            [type]: [description]
        """
        try:
            logger.info('CompanyRepository create ')
            return {"company": "company repo create"}
        except Exception as e:
            logger.error({"error": f"CompanyRepository create : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompanyCreateExcepion(e)

    async def read(self) -> dict:
        """[summary]

        Raises:
            CompaniesReadExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info('CompanyRepository read all')
            return {"company": "company repo read all"}
        except Exception as e:
            logger.error({"error": f"CompanyRepository read all : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompaniesReadExcepion(e)

    async def readById(self, id: str) -> dict:
        """[summary]

        Args:
            id (str): [description]

        Raises:
            CompanyReadByIdExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info(f'CompanyRepository readById : {id}')
            return {"company": f"company repo readById : {id}"}
        except Exception as e:
            logger.error({"error": f"CompanyRepository readById : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompanyReadByIdExcepion(e)

    async def update(self, id: str, data: dict) -> dict:
        """[summary]

        Args:
            id (str): [description]
            data (dict): [description]

        Raises:
            CompanyUpdateExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info(f'CompanyRepository update : {id}')
            return {"company": f"company repo update : {id}"}
        except Exception as e:
            logger.error({"error": f"CompanyRepository update : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompanyUpdateExcepion(e)

    async def delete(self, id):
        pass
