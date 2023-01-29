from app.src.domain.valuesobjects import ValueObject, ValueObjectExcepion, Rules
import re

class ObjectId(ValueObject):
    def __init__(self, value: str):
        self.__value = Rules.run(value)
        pass

    def get(self) -> str:
        return self.__value

class Rules(Rules):

    @staticmethod
    def run(value) -> str:
        regex = r"^[a-fA-F0-9]{24}$"
        if not re.fullmatch(regex, value):
            raise ObjectIdExcepion("ObjectId format not valid")
        return value


class ObjectIdExcepion(ValueObjectExcepion):
    pass