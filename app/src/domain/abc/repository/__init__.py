from abc import ABC, abstractmethod
from app.src.domain.abc.entity import Entity
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.domain.abc.query import Query


class CreateRepository(ABC):
    @abstractmethod
    async def create(self, data: Entity):
        pass


class ReadAllRepository(ABC):

    @abstractmethod
    async def read(self, query: Query):
        pass


class ReadRepository(ABC):

    @abstractmethod
    async def readById(self, data: Entity):
        pass


class UpdateRepository(ABC):

    @abstractmethod
    async def update(self, id: ObjectId, data: Entity):
        pass


class DeleteRepository(ABC):

    @abstractmethod
    async def delete(self, id: ObjectId):
        pass
