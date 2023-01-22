from app.bootstrap.logger import logger
from typing import Union
from app.src.infrastructure.v1.company.entities import Company


class UpdateCompanyAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, data: Union[Company, None] = None):
        """[summary]

        Args:
            id (Union[str, None], optional): [description]. Defaults to None.
            data (dict, optional): [description]. Defaults to {}.
        """
        logger.info(f'[UpdateCompanyAction] Complete loop event : {data.id} {data.to_dict()}')
