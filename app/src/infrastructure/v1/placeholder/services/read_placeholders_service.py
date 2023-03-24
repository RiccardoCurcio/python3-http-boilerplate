from app.src.domain.abc.service import Service
from app.src.infrastructure.v1.placeholder.queries import Placeholder
from app.src.infrastructure.v1.placeholder.exceptions.eventsException import PlaceholderEventExcepion
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import (
    PlaceholdersReadExcepion,
)
from app.src.infrastructure.v1.placeholder.repositories.read_placeholders_repository import (
    ReadPlaceholdersRepository,
)
from app.bootstrap.logger import logger


class ReadPlaceholdersService(Service):
    """[Read placeholders service]

    Args:
        Service ([Service]): [ADS service]
    """

    def __init__(self, repository: ReadPlaceholdersRepository, event: PlaceholderEvent) -> None:
        """[summary]

        Args:
            repository (ReadPlaceholdersRepository): [description]
            event (PlaceholderEvent): [description]
        """
        self.__repo = repository
        self.__event = event
        self.__response: dict[Placeholder | None]

    async def excute(self, query: Placeholder) -> dict[Placeholder | None]:
        """[Execute]

        Args:
            id (str): [id entity to read]

        Raises:
            Exception: [description]

        Returns:
            dict: [to response]
        """

        logger.info("ReadPlaceholdersService excute ")

        try:
            self.__response = await self.__repo.read(query)
        except PlaceholdersReadExcepion as e:
            logger.error(
                {
                    "error": f"ReadPlaceholdersService ReadPlaceholdersRepository read all: {e.__repr__}"
                },
                exc_info=True,
            )
            raise Exception(e)

        try:
            self.__event.dispatch()
        except PlaceholderEventExcepion as e:
            logger.error(
                {"error": f"ReadPlaceholdersService placeholderEvent dispatch: {e.__repr__}"},
                exc_info=True,
            )

        return self.__response
