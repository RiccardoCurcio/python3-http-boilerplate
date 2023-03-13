from app.src.infrastructure.v1.user.queries import User as UserQuery
from app.src.infrastructure.v1.user.entities import User
from app.src.domain.abc.repository import ReadAllRepository
from app.src.infrastructure.v1.user.exceptions.repositoriesException import UsersReadExcepion
from app.bootstrap.logger import logger


class ReadUsersRepository(ReadAllRepository):
    async def read(self, query: UserQuery) -> list[User]:
        """[summary]

        Raises:
            UsersReadExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info('userRepository read all')
            return []
        except Exception as e:
            logger.error({"error": f"userRepository read all : {e.__repr__}"}, exc_info=True)
            raise UsersReadExcepion(e)
