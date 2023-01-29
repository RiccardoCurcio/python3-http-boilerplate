from app.src.domain.valuesobjects import ValueObject, ValueObjectExcepion, Rules
import re


class Email(ValueObject):
    def __init__(self, value: str):
        self.__value = Rules.run(value)
        pass

    def get(self) -> str:
        return self.__value


class Rules(Rules):

    @staticmethod
    def run(value) -> str:
        regex = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        if not re.fullmatch(regex, value):
            raise EmailExcepion("Email format not valid")
        return value


class EmailExcepion(ValueObjectExcepion):
    pass
