from app.src.repository import UpdateRepository
from app.src.v1.exceptions.company.repositories import CompanyUpdateExcepion
import traceback
from app.bootstrap.logger import logger


class UpdateCompanyRepository(UpdateRepository):
    """_summary_

    Args:
        UpdateRepository (_type_): _description_
    """

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
