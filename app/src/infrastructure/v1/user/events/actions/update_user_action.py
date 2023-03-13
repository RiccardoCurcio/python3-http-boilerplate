from app.bootstrap.logger import logger
from typing import Union
from app.src.infrastructure.v1.user.entities import User


class UpdateUserAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, data: Union[User, None] = None):
        """[summary]

        Args:
            id (Union[str, None], optional): [description]. Defaults to None.
            data (dict, optional): [description]. Defaults to {}.
        """
        logger.info(f'[UpdateUserAction] Complete loop event : {data.id} {data.to_dict()}')
