from app.bootstrap.logger import logger
from typing import Union


class CreateCompanyAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, id: Union[str, None] = None, data: dict = {}):
        """[summary]

        Args:
            id (Union[str, None], optional): [description]. Defaults to None.
            data (dict, optional): [description]. Defaults to {}.
        """
        logger.info(f'[CreateCompanyAction] Complete loop event : {data}')
