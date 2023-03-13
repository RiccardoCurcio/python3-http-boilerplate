from typing import Union
from app.src.domain.abc.repository import CreateRepository
from app.src.infrastructure.v1.user.entities import User
from app.src.infrastructure.v1.user.exceptions.repositoriesException import UserCreateExcepion
from app.bootstrap.logger import logger


class CreateUserRepository(CreateRepository):
    async def create(self, data: User) -> Union[User, None]:
        """[summary]

        Args:
            data (dict): [description]

        Raises:
            UserCreateExcepion: [description]

        Returns:
            [type]: [description]
        """
        try:
            logger.info('userRepository create ')
            return data
        except Exception as e:
            logger.error({"error": f"userRepository create : {e.__repr__}"}, exc_info=True)
            raise UserCreateExcepion(e)
