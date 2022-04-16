from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    async def excute(self):
        pass
