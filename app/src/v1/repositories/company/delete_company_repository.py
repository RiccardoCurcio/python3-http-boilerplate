from app.src.repository import DeleteRepository
from app.src.v1.entities.company import Company
from app.src.v1.exceptions.company.repositories import CompanyDeleteExcepion
import traceback
from app.bootstrap.logger import logger


class DeleteCompanyRepository(DeleteRepository):
    """_summary_

    Args:
        DeleteRepository (_type_): _description_
    """

    async def delete(self, data: Company):
        """_summary_

        Args:
            id (_type_): _description_

        Raises:
            CompanyDeleteExcepion: _description_

        Returns:
            _type_: _description_
        """
        try:
            logger.info(f'CompanyRepository delete : {data.id}')
            return {"company": f"company repo delete : {data.id.get()}"}
        except Exception as e:
            logger.error({"error": f"CompanyRepository update : {e.__repr__}"})
            logger.error(traceback.format_exc())
            raise CompanyDeleteExcepion(e)
