from app.bootstrap.logger import logger
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class ReadPlaceholdersAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, data: list[Placeholder] = []):
        """[summary]

        Args:
            id (Union[str, None]): [description]
            data (dict): [description]
        """
        logger.info(f'[ReadPlaceholdersAction] Complete loop event : {data}')
