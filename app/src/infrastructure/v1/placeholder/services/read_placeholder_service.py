from typing import Union
from app.src.domain.abc.service import Service
from app.src.infrastructure.v1.placeholder.exceptions.eventsException import PlaceholderEventExcepion
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import (
    PlaceholderReadByIdExcepion,
)
from app.src.infrastructure.v1.placeholder.repositories.read_placeholder_repository import (
    ReadPlaceholderRepository,
)
from app.bootstrap.logger import logger


class ReadPlaceholderService(Service):
    """[Read placeholder service]

    Args:
        Service ([Service]): [ADS service]
    """

    def __init__(self, repository: ReadPlaceholderRepository, event: PlaceholderEvent) -> None:
        """[summary]

        Args:
            repository (ReadPlaceholderRepository): [description]
            event (PlaceholderEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: Placeholder) -> Union[Placeholder, None]:
        """[Execute]

        Args:
            id (str): [id entity to read]

        Raises:
            Exception: [description]

        Returns:
            dict: [to response]
        """

        response = {}

        logger.info(f"ReadplaceholderService excute id={data.id}")

        try:
            response = await self.__repo.readById(data=data)
        except PlaceholderReadByIdExcepion as e:
            logger.error(
                {"error": f"ReadplaceholderService ReadPlaceholderRepository readById: {e.__repr__}"},
                exc_info=True,
            )
            raise Exception(e)

        try:
            self.__event.dispatch(data=data)
        except PlaceholderEventExcepion as e:
            logger.error(
                {"error": f"ReadplaceholderService placeholderEvent dispatch: {e.__repr__}"},
                exc_info=True,
            )

        return response
