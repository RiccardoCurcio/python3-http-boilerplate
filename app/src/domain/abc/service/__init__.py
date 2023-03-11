from abc import ABC, abstractmethod
from app.src.domain.abc.entity import Entity
from typing import Union


class Service(ABC):
    @abstractmethod
    async def excute(self, data: Entity | None) -> Union[Entity, None]:
        pass
