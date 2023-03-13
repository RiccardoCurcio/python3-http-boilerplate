from typing import Union
from app.src.domain.abc.repository import ReadRepository
from app.src.infrastructure.v1.user.entities import User
from app.src.infrastructure.v1.user.exceptions.repositoriesException import UserReadByIdExcepion
from app.bootstrap.logger import logger


class ReadUserRepository(ReadRepository):

    async def readById(self, data: User) -> Union[User, None]:
        """[summary]

        Args:
            id (str): [description]

        Raises:
            userReadByIdExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info(f'userRepository readById : {data.id}')
            return data
        except Exception as e:
            logger.error({"error": f"userRepository readById : {e.__repr__}"}, exc_info=True)
            raise UserReadByIdExcepion(e)
