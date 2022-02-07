from app.bootstrap.logger import logger
from typing import Union


class ReadCompaniesAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, id: Union[str, None], data: dict):
        """[summary]

        Args:
            id (Union[str, None]): [description]
            data (dict): [description]
        """
        logger.info(f'[ReadCompaniesAction] Complete loop event : {data}')
