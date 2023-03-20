from app.src.domain.abc.gateway import ReadAllGateway
from app.src.infrastructure.v1.placeholder.queries import Placeholder as Query


class ReadPaceholdersGateway(ReadAllGateway):
    async def call(self, query: Query) -> list[dict]:
        return await self.__call_service(query)

    async def __call_service(self, query: Query):
        return [
            {
                "id": "617c4d302bdaae79da0a6778",
                "name": "pippo",
                "vatNumber": "0000",
                "phones": ["3492256745", "0039 (333) 3423456", "+23 435 7865345"],
                "emails": ["ere@pino.com"],
            },
            {
                "id": "617c4d302bdaae79da0a6779",
                "name": "pippo",
                "vatNumber": "0000",
                "phones": ["3492256745", "0039 (333) 3423456", "+23 435 7865345"],
                "emails": ["ere@pino.com"],
            },
            {
                "id": "617c4d302bdaae79da0a6770",
                "name": "pippo",
                "vatNumber": "0000",
                "phones": ["3492256745", "0039 (333) 3423456", "+23 435 7865345"],
                "emails": ["ere@pino.com"],
            },
        ]
