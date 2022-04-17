from typing import Union
from app.src.repository import CreateRepository
from app.src.v1.entities.company import Company
from app.src.v1.exceptions.company.repositories import CompanyCreateExcepion
import traceback
from app.bootstrap.logger import logger


class CreateCompanyRepository(CreateRepository):
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
