from app.src.domain.abc.service import Service
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.user.entities import User
from app.src.infrastructure.v1.user.exceptions.eventsException import UserEventExcepion
from app.src.infrastructure.v1.user.events import UserEvent
from app.src.infrastructure.v1.user.exceptions.repositoriesException import (
    UserUpdateExcepion,
)
from app.src.infrastructure.v1.user.repositories.update_user_repository import (
    UpdateUserRepository,
)


class UpdateUserService(Service):
    """[Update user service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(self, repository: UpdateUserRepository, event: UserEvent) -> None:
        """[summary]

        Args:
            repository (UpdateUserRepository): [description]
            event (UserEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: User) -> dict:
        """[Update user service]

        Args:
            id (str): [id entity to update]
            data (dict): [data to update]

        Raises:
            Exception: []

        Returns:
            dict: [to reponse]
        """
        response = {}
        logger.info(f"UpdateuserService excute id={data.id}")

        try:
            response = await self.__repo.update(data=data)
        except UserUpdateExcepion as e:
            logger.error(
                {
                    "error": f"UpdateuserService UpdateUserRepository update: {e.__repr__}"
                },
                exc_info=True,
            )
            raise Exception(e)
        try:
            self.__event.dispatch(data=data)
        except UserEventExcepion as e:
            logger.error(
                {"error": f"UpdateuserService userEvent dispatch: {e.__repr__}"},
                exc_info=True,
            )

        return response
