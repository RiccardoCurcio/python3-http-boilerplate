from typing import Union
from app.src.domain.abc.service import Service
from app.src.infrastructure.v1.user.exceptions.eventsException import UserEventExcepion
from app.src.infrastructure.v1.user.events import UserEvent
from app.src.infrastructure.v1.user.entities import User
from app.src.infrastructure.v1.user.exceptions.repositoriesException import (
    UserReadByIdExcepion,
)
from app.src.infrastructure.v1.user.repositories.read_user_repository import (
    ReadUserRepository,
)
from app.bootstrap.logger import logger


class ReadUserService(Service):
    """[Read user service]

    Args:
        Service ([Service]): [ADS service]
    """

    def __init__(self, repository: ReadUserRepository, event: UserEvent) -> None:
        """[summary]

        Args:
            repository (ReadUserRepository): [description]
            event (UserEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: User) -> Union[User, None]:
        """[Execute]

        Args:
            id (str): [id entity to read]

        Raises:
            Exception: [description]

        Returns:
            dict: [to response]
        """

        response = {}

        logger.info(f"ReaduserService excute id={data.id}")

        try:
            response = await self.__repo.readById(data=data)
        except UserReadByIdExcepion as e:
            logger.error(
                {"error": f"ReaduserService ReadUserRepository readById: {e.__repr__}"},
                exc_info=True,
            )
            raise Exception(e)

        try:
            self.__event.dispatch(data=data)
        except UserEventExcepion as e:
            logger.error(
                {"error": f"ReaduserService userEvent dispatch: {e.__repr__}"},
                exc_info=True,
            )

        return response
