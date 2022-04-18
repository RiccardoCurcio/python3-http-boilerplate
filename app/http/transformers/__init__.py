from abc import ABC, abstractmethod


class Tranformer(ABC):

    @staticmethod
    @abstractmethod
    def transform() -> dict:
        pass
