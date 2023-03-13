from app.bootstrap.logger import logger
from app.src.infrastructure.v1.user.entities import User


class ReadUserAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, data: User):
        """[summary]

        Args:
            id (Union[str, None]): [description]
            data (dict): [description]
        """
        logger.info(f'[ReadUserAction] Complete loop event : {data.id} {data.to_dict()}')
