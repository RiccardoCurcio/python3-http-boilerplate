from bootstrap.logger import logger
from typing import Union


class ReadCompanyAction:
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
        logger.info(f'[ReadCompanyAction] Complete loop event : {id} {data}')
