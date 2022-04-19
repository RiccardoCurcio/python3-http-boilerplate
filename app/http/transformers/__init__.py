from abc import ABC, abstractstaticmethod


class Tranformer(ABC):

    @staticmethod
    @abstractstaticmethod
    def transform() -> dict:
        pass
