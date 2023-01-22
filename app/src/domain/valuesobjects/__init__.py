from abc import ABC, abstractmethod
from typing import Any


class ValueObject(ABC):
    @abstractmethod
    def get(self) -> Any:
        pass


class Rules(ABC):
    @staticmethod
    @abstractmethod
    def run(value) -> bool:
        pass


class ValueObjectExcepion(Exception):
    pass
