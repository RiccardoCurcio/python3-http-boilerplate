from abc import ABC, abstractmethod


class Event(ABC):
    @abstractmethod
    async def dispatch(self, eventName: str) -> None:
        pass


class CompanyEventExcepion(Exception):
    pass
