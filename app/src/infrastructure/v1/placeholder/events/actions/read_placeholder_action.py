from app.bootstrap.logger import logger
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class ReadPlaceholderAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, data: Placeholder):
        """[summary]

        Args:
            id (Union[str, None]): [description]
            data (dict): [description]
        """
        logger.info(f'[ReadPlaceholderAction] Complete loop event : {data.id} {data.to_dict()}')
