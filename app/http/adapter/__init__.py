from abc import ABC, abstractmethod
from aiohttp.web_request import Request


class Adapter(ABC):

    @abstractmethod
    def adapt(self, request: Request):
        pass
