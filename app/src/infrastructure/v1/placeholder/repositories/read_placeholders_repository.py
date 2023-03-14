from app.src.infrastructure.v1.placeholder.queries import Placeholder as PlaceholderQuery
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.domain.abc.repository import ReadAllRepository
from app.src.infrastructure.v1.placeholder.gateways.read_placeholders_gateway import ReadPaceholdersGateway
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import PlaceholdersReadExcepion
from app.src.infrastructure.v1.placeholder.mapper.mapper import Mapper
from app.bootstrap.logger import logger


class ReadPlaceholdersRepository(ReadAllRepository):
    def __init__(
        self, gateway: ReadPaceholdersGateway
    ) -> None:
        """_summary_

        Args:
            gateway (ReadPaceholderGateway): _description_
        """
        self.__gateway = gateway

    async def read(self, query: PlaceholderQuery) -> list[Placeholder]:
        """[summary]

        Raises:
            PlaceholdersReadExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info('placeholderRepository read all')
            print(Mapper.map_list(await self.__gateway.call(query)))
            return Mapper.map_list(await self.__gateway.call(query))
        except Exception as e:
            logger.error({"error": f"placeholderRepository read all : {e.__repr__}"}, exc_info=True)
            raise PlaceholdersReadExcepion(e)
