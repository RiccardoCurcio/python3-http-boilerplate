from typing import Union
from app.src.domain.abc.repository import UpdateRepository
from app.src.infrastructure.v1.user.exceptions.repositoriesException import UserUpdateExcepion
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.user.entities import User


class UpdateUserRepository(UpdateRepository):
    """_summary_

    Args:
        UpdateRepository (_type_): _description_
    """

    async def update(self, data: Union[User, None]) -> Union[User, None]:
        """[summary]

        Args:
            id (str): [description]
            data (dict): [description]

        Raises:
            UserUpdateExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info(f'userRepository update : {data.id}')
            return data
        except Exception as e:
            logger.error({"error": f"userRepository update : {e.__repr__}"}, exc_info=True)
            raise UserUpdateExcepion(e)
