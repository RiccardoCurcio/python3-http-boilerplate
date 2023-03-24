from app.src.domain.abc.service import Service
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.placeholder.exceptions.eventsException import (
    PlaceholderEventExcepion,
)
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import (
    PlaceholderDeleteExcepion,
)
from app.src.infrastructure.v1.placeholder.repositories.delete_placeholder_repository import (
    DeletePlaceholderRepository,
)
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class DeletePlaceholderService(Service):
    """[Delete placeholder service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(
        self, repository: DeletePlaceholderRepository, event: PlaceholderEvent
    ) -> None:
        """[summary]

        Args:
            repository (DeletePlaceholderRepository): [description]
            event (PlaceholderEvent): [description]
        """
        self.__repo: DeletePlaceholderRepository = repository
        self.__event: PlaceholderEvent = event
        self.__response: dict = {}

    async def excute(self, data: Placeholder) -> dict:
        """[Delete placeholder service]

        Args:
            id (str): [id entity to delete]

        Raises:
            Exception: []

        Returns:
            dict: [to reponse]
        """

        logger.info(f"DeleteplaceholderService excute id={data.id}")

        try:
            self.__response = await self.__repo.delete(data=data)
        except PlaceholderDeleteExcepion as e:
            logger.error(
                {
                    "error": f"DeleteplaceholderService DeletePlaceholderRepository delete: {e.__repr__}"
                },
                exc_info=True,
            )
            raise Exception(e)
        try:
            self.__event.dispatch(data=data)
        except PlaceholderEventExcepion as e:
            logger.error(
                {
                    "error": f"DeleteplaceholderService placeholderEvent dispatch: {e.__repr__}"
                },
                exc_info=True,
            )

        return self.__response
