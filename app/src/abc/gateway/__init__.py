from abc import ABC, abstractmethod


class Gateway(ABC):
    @abstractmethod
    async def call(self) -> dict:
        pass
