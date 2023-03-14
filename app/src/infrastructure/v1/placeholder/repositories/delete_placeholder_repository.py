from app.src.domain.abc.repository import DeleteRepository
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.infrastructure.v1.placeholder.gateways.delete_placeholder_gateway import DeletePaceholderGateway
from app.src.infrastructure.v1.placeholder.exceptions.repositoriesException import PlaceholderDeleteExcepion
from app.bootstrap.logger import logger


class DeletePlaceholderRepository(DeleteRepository):
    def __init__(
        self, gateway: DeletePaceholderGateway
    ) -> None:
        """_summary_

        Args:
            gateway (DeletePaceholderGateway): _description_
        """
        self.__gateway = gateway

    async def delete(self, data: Placeholder) -> dict:
        """_summary_

        Args:
            id (_type_): _description_

        Raises:
            PlaceholderDeleteExcepion: _description_

        Returns:
            _type_: _description_
        """
        try:
            logger.info(f'placeholderRepository delete : {data.id}')
            return await self.__gateway.call(data)
        except Exception as e:
            logger.error({"error": f"placeholderRepository update : {e.__repr__}"}, exc_info=True)
            raise PlaceholderDeleteExcepion(e)
