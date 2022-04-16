from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    async def create(self, data):
        pass

    @abstractmethod
    async def read(self):
        pass

    @abstractmethod
    async def readById(self, id):
        pass

    @abstractmethod
    async def update(self, id, data):
        pass

    @abstractmethod
    async def delete(self, id):
        pass
