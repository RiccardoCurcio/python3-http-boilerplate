from app.src.domain.abc.gateway import CreateGateway
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class UpdatePaceholderGateway(CreateGateway):
    async def call(self, data: Placeholder) -> dict:
        return await self.__call_service(data)

    async def __call_service(self, data: Placeholder):
        return {
            "id": data.id.get(),
            "name": data.name.get(),
            "vatNumber": data.vatNumber.get(),
            "phones": map(lambda item: item.get(), data.phones),
            "emails": map(lambda item: item.get(), data.emails),
        }
