from app.src.domain.abc.service import Service
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.user.exceptions.eventsException import UserEventExcepion
from app.src.infrastructure.v1.user.events import UserEvent
from app.src.infrastructure.v1.user.exceptions.repositoriesException import (
    UserDeleteExcepion,
)
from app.src.infrastructure.v1.user.repositories.delete_user_repository import (
    DeleteUserRepository,
)
from app.src.infrastructure.v1.user.entities import User


class DeleteUserService(Service):
    """[Delete user service]

    Args:
        Service ([Service]): [ABS service]
    """

    def __init__(self, repository: DeleteUserRepository, event: UserEvent) -> None:
        """[summary]

        Args:
            repository (DeleteUserRepository): [description]
            event (UserEvent): [description]
        """
        self.__repo = repository
        self.__event = event

    async def excute(self, data: User) -> dict:
        """[Delete user service]

        Args:
            id (str): [id entity to delete]

        Raises:
            Exception: []

        Returns:
            dict: [to reponse]
        """
        response = {}
        logger.info(f"DeleteuserService excute id={data.id}")

        try:
            response = await self.__repo.delete(data=data)
        except UserDeleteExcepion as e:
            logger.error(
                {
                    "error": f"DeleteuserService DeleteUserRepository delete: {e.__repr__}"
                },
                exc_info=True,
            )
            raise Exception(e)
        try:
            self.__event.dispatch(data=data)
        except UserEventExcepion as e:
            logger.error(
                {"error": f"DeleteuserService userEvent dispatch: {e.__repr__}"},
                exc_info=True,
            )

        return response
