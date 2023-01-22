from app.bootstrap.logger import logger
from app.src.infrastructure.v1.company.entities import Company
from typing import Union


class CreateCompanyAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, id: Union[str, None] = None, data: Company = None):
        """[summary]

        Args:
            id (Union[str, None], optional): [description]. Defaults to None.
            data (dict, optional): [description]. Defaults to {}.
        """
        logger.info(f'[CreateCompanyAction] Complete loop event : {data.to_dict()}')
