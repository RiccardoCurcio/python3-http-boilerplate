from app.bootstrap.logger import logger
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from typing import Union


class CreatePlaceholderAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, id: Union[str, None] = None, data: Placeholder = None):
        """[summary]

        Args:
            id (Union[str, None], optional): [description]. Defaults to None.
            data (dict, optional): [description]. Defaults to {}.
        """
        logger.info(f'[CreateplaceholderAction] Complete loop event : {data.to_dict()}')
