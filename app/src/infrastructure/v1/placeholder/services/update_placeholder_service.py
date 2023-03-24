from app.src.domain.abc.service import Service
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.infrastructure.v1.placeholder.exceptions.eventsException import (
    PlaceholderEventExcepion,
)
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import (
    PlaceholderUpdateExcepion,
)
from app.src.infrastructure.v1.placeholder.repositories.update_placeholder_repository import (
    UpdatePlaceholderRepository,
)


class UpdatePlaceholderService(Service):
    """[Update placeholder service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(
        self, repository: UpdatePlaceholderRepository, event: PlaceholderEvent
    ) -> None:
        """[summary]

        Args:
            repository (UpdatePlaceholderRepository): [description]
            event (PlaceholderEvent): [description]
        """
        self.__repo: UpdatePlaceholderRepository = repository
        self.__event: PlaceholderEvent = event
        self.__response: Placeholder | None = None

    async def excute(self, data: Placeholder) -> Placeholder | None:
        """[Update placeholder service]

        Args:
            id (str): [id entity to update]
            data (dict): [data to update]

        Raises:
            Exception: []

        Returns:
            dict: [to reponse]
        """
        logger.info(f"UpdateplaceholderService excute id={data.id}")

        try:
            self.__response = await self.__repo.update(data=data)
        except PlaceholderUpdateExcepion as e:
            logger.error(
                {
                    "error": f"UpdateplaceholderService UpdatePlaceholderRepository update: {e.__repr__}"
                },
                exc_info=True,
            )
            raise Exception(e)
        try:
            self.__event.dispatch(data=data)
        except PlaceholderEventExcepion as e:
            logger.error(
                {
                    "error": f"UpdateplaceholderService placeholderEvent dispatch: {e.__repr__}"
                },
                exc_info=True,
            )

        return self.__response
