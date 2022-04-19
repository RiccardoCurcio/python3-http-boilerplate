from typing import List
from app.src.v1.queries.company import Company as CompanyQuery
from app.src.v1.entities.company import Company
from app.src.repository import ReadAllRepository
from app.src.v1.exceptions.company.repositories import CompaniesReadExcepion
import traceback
from app.bootstrap.logger import logger


class ReadCompaniesRepository(ReadAllRepository):
    async def read(self, query: CompanyQuery) -> List[Company]:
        """[summary]

        Raises:
            CompaniesReadExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info('CompanyRepository read all')
            return []
        except Exception as e:
            logger.error({"error": f"CompanyRepository read all : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompaniesReadExcepion(e)
