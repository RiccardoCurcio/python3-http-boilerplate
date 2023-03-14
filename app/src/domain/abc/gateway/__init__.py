from abc import ABC, abstractmethod
from app.src.domain.abc.entity import Entity
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.domain.abc.query import Query


class CreateGateway(ABC):
    @abstractmethod
    async def call(self, data: Entity) -> dict:
        pass


class ReadAllGateway(ABC):

    @abstractmethod
    async def call(self, query: Query) -> list[dict]:
        pass


class ReadGateway(ABC):

    @abstractmethod
    async def call(self, data: Entity) -> dict:
        pass


class UpdateGateway(ABC):

    @abstractmethod
    async def call(self, data: Entity) -> dict:
        pass


class DeleteGateway(ABC):

    @abstractmethod
    async def call(self, id: ObjectId) -> dict:
        pass
