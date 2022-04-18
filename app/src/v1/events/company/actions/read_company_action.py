from app.bootstrap.logger import logger
from app.src.v1.entities.company import Company


class ReadCompanyAction:
    """[summary]
    """
    def __init__(self):
        """[summary]
        """
        pass

    def run(self, data: Company):
        """[summary]

        Args:
            id (Union[str, None]): [description]
            data (dict): [description]
        """
        logger.info(f'[ReadCompanyAction] Complete loop event : {data.id} {data.to_dict()}')
