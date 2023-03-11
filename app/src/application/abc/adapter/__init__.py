from typing import Union
from abc import ABC, abstractmethod
from app.src.domain.abc.entity import Entity
from app.src.domain.abc.query import Query


class Adapter(ABC):
    @abstractmethod
    async def adapt(self) -> Union[Entity, Query]:
        pass
