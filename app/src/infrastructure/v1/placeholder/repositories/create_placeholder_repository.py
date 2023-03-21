from typing import Union
from app.src.domain.abc.repository import CreateRepository
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import PlaceholderCreateExcepion
from app.src.infrastructure.v1.placeholder.gateways.create_placeholder_gateway import CreatePaceholderGateway
from app.src.infrastructure.v1.placeholder.mapper import Mapper
from app.bootstrap.logger import logger


class CreatePlaceholderRepository(CreateRepository):

    def __init__(
        self, gateway: CreatePaceholderGateway
    ) -> None:
        """_summary_

        Args:
            gateway (CreatePaceholderGateway): _description_
        """
        self.__gateway = gateway

    async def create(self, data: Placeholder) -> Union[Placeholder, None]:
        """[summary]

        Args:
            data (dict): [description]

        Raises:
            PlaceholderCreateExcepion: [description]

        Returns:
            [type]: [description]
        """
        try:
            logger.info('placeholderRepository create ')
            return Mapper.map(await self.__gateway.call(data))
        except Exception as e:
            logger.error({"error": f"placeholderRepository create : {e.__repr__}"}, exc_info=True)
            raise PlaceholderCreateExcepion(e)
