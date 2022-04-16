from typing import Union
from app.src.repository import Repository
from app.src.v1.entities.company import Company
from app.src.v1.exceptions.company.repositories import CompanyUpdateExcepion, CompanyReadByIdExcepion, CompaniesReadExcepion, CompanyCreateExcepion, CompanyDeleteExcepion
import traceback
from app.bootstrap.logger import logger


class CompanyRepository(Repository):
    async def create(self, data: Company) -> Union[Company, None]:
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
            return data
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
        try:
            logger.info(f'CompanyRepository delete : {id}')
            return {"company": f"company repo delete : {id}"}
        except Exception as e:
            logger.error({"error": f"CompanyRepository update : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompanyDeleteExcepion(e)
