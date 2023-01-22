from typing import Union
from abc import ABC, abstractmethod
from aiohttp.web_request import Request
from app.src.domain.abc.entity import Entity
from app.src.domain.abc.query import Query


class Adapter(ABC):

    @abstractmethod
    def adapt(self, request: Request) -> Union[Entity, Query]:
        pass
