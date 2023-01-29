from app.src.domain.valuesobjects import ValueObject, ValueObjectExcepion, Rules
import re

class PhoneNumber(ValueObject):
    def __init__(self, value: str):
        self.__value = Rules.run(value)
        pass

    def get(self) -> str:
        return self.__value

class Rules(Rules):

    @staticmethod
    def run(value) -> str:
        regex = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
        if not re.fullmatch(regex, value):
            raise PhoneNumberExcepion("PhoneNumber format not valid")
        return value


class PhoneNumberExcepion(ValueObjectExcepion):
    pass