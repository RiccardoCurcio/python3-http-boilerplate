from app.src.domain.abc.gateway import DeleteGateway
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class DeletePaceholderGateway(DeleteGateway):
    async def call(self, data: Placeholder) -> dict:
        return await self.__call_service(data)

    async def __call_service(self, data: Placeholder):
        return {"id": data.id.get()}
