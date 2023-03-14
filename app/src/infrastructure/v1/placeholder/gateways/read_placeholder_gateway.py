from app.src.domain.abc.gateway import ReadGateway
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.domain.valuesobjects.ObjectId import ObjectId


class ReadPaceholderGateway(ReadGateway):
    async def call(self, data: Placeholder) -> dict:
        data.id = ObjectId("617c4d302bdaae79da0a6778")
        return {
            "id": data.id.get(),
            "name": "pippo",
            "vatNumber": "0000",
            "phones": ["3492256745", "0039 (333) 3423456", "+23 435 7865345"],
            "emails": ["ere@pino.com"],
        }
