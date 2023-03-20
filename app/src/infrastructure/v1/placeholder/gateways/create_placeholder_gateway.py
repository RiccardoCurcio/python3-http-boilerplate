from app.src.domain.abc.gateway import CreateGateway
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.domain.valuesobjects.ObjectId import ObjectId


class CreatePaceholderGateway(CreateGateway):
    async def call(self, data: Placeholder) -> dict:
        return await self.__call_service(data)

    async def __call_service(self, data: Placeholder):
        data.id = ObjectId("617c4d302bdaae79da0a6778")
        return {
            "id": data.id.get(),
            "name": data.name.get(),
            "vatNumber": data.vatNumber.get(),
            "phones": map(lambda item: item.get(), data.phones),
            "emails": map(lambda item: item.get(), data.emails),
        }
