from abc import ABC, abstractclassmethod


class Entity(ABC):

    @abstractclassmethod
    def to_dict(self) -> dict:
        pass
