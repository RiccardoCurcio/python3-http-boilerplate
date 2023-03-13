from app.src.domain.abc.repository import DeleteRepository
from app.src.infrastructure.v1.user.entities import User
from app.src.infrastructure.v1.user.exceptions.repositoriesException import UserDeleteExcepion
from app.bootstrap.logger import logger


class DeleteUserRepository(DeleteRepository):
    """_summary_

    Args:
        DeleteRepository (_type_): _description_
    """

    async def delete(self, data: User) -> dict:
        """_summary_

        Args:
            id (_type_): _description_

        Raises:
            UserDeleteExcepion: _description_

        Returns:
            _type_: _description_
        """
        try:
            logger.info(f'userRepository delete : {data.id}')
            return {"user": f"user repo delete : {data.id.get()}"}
        except Exception as e:
            logger.error({"error": f"userRepository update : {e.__repr__}"}, exc_info=True)
            raise UserDeleteExcepion(e)
