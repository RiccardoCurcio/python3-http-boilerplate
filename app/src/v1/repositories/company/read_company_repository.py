from typing import Union
from app.src.repository import ReadRepository
from app.src.v1.entities.company import Company
from app.src.v1.exceptions.company.repositories import CompanyReadByIdExcepion
import traceback
from app.bootstrap.logger import logger


class ReadCompanyRepository(ReadRepository):

    async def readById(self, data: Company) -> Union[Company, None]:
        """[summary]

        Args:
            id (str): [description]

        Raises:
            CompanyReadByIdExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info(f'CompanyRepository readById : {data.id}')
            return data
        except Exception as e:
            logger.error({"error": f"CompanyRepository readById : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompanyReadByIdExcepion(e)
