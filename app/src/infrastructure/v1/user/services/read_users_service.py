from app.src.domain.abc.service import Service
from app.src.infrastructure.v1.user.queries import User
from app.src.infrastructure.v1.user.exceptions.eventsException import UserEventExcepion
from app.src.infrastructure.v1.user.events import UserEvent
from app.src.infrastructure.v1.user.exceptions.repositoriesException import (
    UsersReadExcepion,
)
from app.src.infrastructure.v1.user.repositories.read_users_repository import (
    ReadUsersRepository,
)
from app.bootstrap.logger import logger


class ReadUsersService(Service):
    """[Read users service]

    Args:
        Service ([Service]): [ADS service]
    """

    def __init__(self, repository: ReadUsersRepository, event: UserEvent) -> None:
        """[summary]

        Args:
            repository (ReadUsersRepository): [description]
            event (UserEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, query: User) -> dict:
        """[Execute]

        Args:
            id (str): [id entity to read]

        Raises:
            Exception: [description]

        Returns:
            dict: [to response]
        """

        response = {}

        logger.info("ReadUsersService excute ")

        try:
            response = await self.__repo.read(query)
        except UsersReadExcepion as e:
            logger.error(
                {
                    "error": f"ReadUsersService ReadUsersRepository read all: {e.__repr__}"
                },
                exc_info=True,
            )
            raise Exception(e)

        try:
            self.__event.dispatch()
        except UserEventExcepion as e:
            logger.error(
                {"error": f"ReadUsersService userEvent dispatch: {e.__repr__}"},
                exc_info=True,
            )

        return response
