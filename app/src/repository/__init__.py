from abc import ABC, abstractmethod


class CreateRepository(ABC):
    @abstractmethod
    async def create(self, data):
        pass


class ReadAllRepository(ABC):

    @abstractmethod
    async def read(self):
        pass


class ReadRepository(ABC):

    @abstractmethod
    async def readById(self, id):
        pass


class UpdateRepository(ABC):

    @abstractmethod
    async def update(self, id, data):
        pass


class DeleteRepository(ABC):

    @abstractmethod
    async def delete(self, id):
        pass
