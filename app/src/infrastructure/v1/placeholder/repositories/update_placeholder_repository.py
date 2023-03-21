from typing import Union
from app.src.domain.abc.repository import UpdateRepository
from app.src.infrastructure.v1.placeholder.gateways.update_placeholder_gateway import UpdatePaceholderGateway
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import PlaceholderUpdateExcepion
from app.src.infrastructure.v1.placeholder.mapper import Mapper
from app.bootstrap.logger import logger
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class UpdatePlaceholderRepository(UpdateRepository):
    def __init__(
        self, gateway: UpdatePaceholderGateway
    ) -> None:
        """_summary_

        Args:
            gateway (UpdatePaceholderGateway): _description_
        """
        self.__gateway = gateway

    async def update(self, data: Union[Placeholder, None]) -> Union[Placeholder, None]:
        """[summary]

        Args:
            id (str): [description]
            data (dict): [description]

        Raises:
            PlaceholderUpdateExcepion: [description]

        Returns:
            dict: [description]
        """
        try:
            logger.info(f'placeholderRepository update : {data.id}')
            return Mapper.map(await self.__gateway.call(data))
        except Exception as e:
            logger.error({"error": f"placeholderRepository update : {e.__repr__}"}, exc_info=True)
            raise PlaceholderUpdateExcepion(e)
