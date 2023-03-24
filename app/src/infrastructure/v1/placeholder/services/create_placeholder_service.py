from app.src.domain.abc.service import Service
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.infrastructure.v1.placeholder.exceptions.eventsException import PlaceholderEventExcepion
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import (
    PlaceholderCreateExcepion,
)
from app.src.infrastructure.v1.placeholder.repositories.create_placeholder_repository import (
    CreatePlaceholderRepository,
)


class CreatePlaceholderService(Service):
    """[Create placeholder service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(
        self, repository: CreatePlaceholderRepository, event: PlaceholderEvent
    ) -> None:
        """[summary]

        Args:
            repository (CreatePlaceholderRepository): [description]
            event (placeholderEvent): [description]
        """
        self.__repo: CreatePlaceholderRepository = repository
        self.__event: PlaceholderEvent = event
        self.__response: Placeholder | None = None

    async def excute(self, data: Placeholder) -> Placeholder | None:
        """_summary_

        Args:
            data (placeholder): _description_

        Raises:
            Exception: _description_

        Returns:
            Union[Placeholder, None]: _description_
        """
        
        logger.info("CreateplaceholderService excute")

        try:
            self.__response = await self.__repo.create(data=data)
        except PlaceholderCreateExcepion as e:
            logger.error(
                {
                    "error": f"CreateplaceholderService placeholderRepository create: {e.__repr__}"
                },
                exc_info=True
            )
            raise Exception(e)
        try:
            self.__event.dispatch(data=data)
        except PlaceholderEventExcepion as e:
            logger.error(
                {"error": f"CreateplaceholderService placeholderEvent dispatch: {e.__repr__}"},
                exc_info=True
            )

        return self.__response
