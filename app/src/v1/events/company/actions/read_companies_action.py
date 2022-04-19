from app.bootstrap.logger import logger
from typing import List
from app.src.v1.entities.company import Company


class ReadCompaniesAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, data: List[Company] = []):
        """[summary]

        Args:
            id (Union[str, None]): [description]
            data (dict): [description]
        """
        logger.info(f'[ReadCompaniesAction] Complete loop event : {data}')
