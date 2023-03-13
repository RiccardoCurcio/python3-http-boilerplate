from app.bootstrap.logger import logger
from app.src.infrastructure.v1.user.entities import User
from typing import Union


class CreateUserAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, id: Union[str, None] = None, data: User = None):
        """[summary]

        Args:
            id (Union[str, None], optional): [description]. Defaults to None.
            data (dict, optional): [description]. Defaults to {}.
        """
        logger.info(f'[CreateuserAction] Complete loop event : {data.to_dict()}')
