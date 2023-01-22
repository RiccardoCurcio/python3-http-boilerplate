from typing import Union
from app.src.domain.abc.repository import UpdateRepository
from app.src.infrastructure.v1.company.exceptions.repositories import CompanyUpdateExcepion
import traceback
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.company.entities import Company


class UpdateCompanyRepository(UpdateRepository):
    """_summary_

    Args:
        UpdateRepository (_type_): _description_
    """

    async def update(self, data: Union[Company, None]) -> Union[Company, None]:
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
            logger.info(f'CompanyRepository update : {data.id}')
            return data
        except Exception as e:
            logger.error({"error": f"CompanyRepository update : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompanyUpdateExcepion(e)