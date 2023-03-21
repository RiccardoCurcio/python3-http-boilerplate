from typing import Union
from app.src.domain.abc.repository import ReadRepository
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.infrastructure.v1.placeholder.gateways.read_placeholder_gateway import ReadPaceholderGateway
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import PlaceholderReadByIdExcepion
from app.src.infrastructure.v1.placeholder.mapper import Mapper
from app.bootstrap.logger import logger


class ReadPlaceholderRepository(ReadRepository):

    def __init__(
        self, gateway: ReadPaceholderGateway
    ) -> None:
        """_summary_

        Args:
            gateway (ReadPaceholderGateway): _description_
        """
        self.__gateway = gateway

    async def readById(self, data: Placeholder) -> Union[Placeholder, None]:
        """[summary]

        Args:
            id (str): [description]

        Raises:
            placeholderReadByIdExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info(f'placeholderRepository readById : {data.id}')
            return Mapper.map(await self.__gateway.call(data))
        except Exception as e:
            logger.error({"error": f"placeholderRepository readById : {e.__repr__}"}, exc_info=True)
            raise PlaceholderReadByIdExcepion(e)
