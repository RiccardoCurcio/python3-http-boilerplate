from abc import ABC, abstractmethod

from app.src.domain.abc.entity import Entity


class Tranformer(ABC):

    @staticmethod
    @abstractmethod
    def transform(data: Entity) -> dict:
        pass
