from app.bootstrap.logger import logger
from app.src.infrastructure.v1.user.entities import User


class ReadUsersAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, data: list[User] = []):
        """[summary]

        Args:
            id (Union[str, None]): [description]
            data (dict): [description]
        """
        logger.info(f'[ReadUsersAction] Complete loop event : {data}')
