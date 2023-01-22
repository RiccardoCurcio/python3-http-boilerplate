from typing import Union
from app.src.domain.abc.repository import CreateRepository
from app.src.infrastructure.v1.company.entities import Company
from app.src.infrastructure.v1.company.exceptions.repositories import CompanyCreateExcepion
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
