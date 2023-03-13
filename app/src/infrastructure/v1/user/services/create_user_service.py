from typing import Union
from app.src.domain.abc.service import Service
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.user.entities import User
from app.src.infrastructure.v1.user.exceptions.eventsException import UserEventExcepion
from app.src.infrastructure.v1.user.events import UserEvent
from app.src.infrastructure.v1.user.exceptions.repositoriesException import (
    UserCreateExcepion,
)
from app.src.infrastructure.v1.user.repositories.create_user_repository import (
    CreateUserRepository,
)


class CreateUserService(Service):
    """[Create user service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(
        self, repository: CreateUserRepository, event: UserEvent
    ) -> None:
        """[summary]

        Args:
            repository (CreateUserRepository): [description]
            event (userEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: User) -> Union[User, None]:
        """_summary_

        Args:
            data (user): _description_

        Raises:
            Exception: _description_

        Returns:
            Union[User, None]: _description_
        """
        response: Union[User, None] = None
        logger.info("CreateuserService excute")

        try:
            response = await self.__repo.create(data=data)
        except UserCreateExcepion as e:
            logger.error(
                {
                    "error": f"CreateuserService userRepository create: {e.__repr__}"
                },
                exc_info=True
            )
            raise Exception(e)
        try:
            self.__event.dispatch(data=data)
        except UserEventExcepion as e:
            logger.error(
                {"error": f"CreateuserService userEvent dispatch: {e.__repr__}"},
                exc_info=True
            )

        return response
