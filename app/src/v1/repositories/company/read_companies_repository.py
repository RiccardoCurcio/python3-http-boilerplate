from app.src.repository import ReadAllRepository
from app.src.v1.exceptions.company.repositories import CompaniesReadExcepion
import traceback
from app.bootstrap.logger import logger


class ReadCompaniesRepository(ReadAllRepository):
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
