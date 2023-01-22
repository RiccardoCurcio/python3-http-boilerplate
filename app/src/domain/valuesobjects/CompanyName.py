from app.src.domain.valuesobjects import ValueObject, ValueObjectExcepion, Rules
import re


class CompanyName(ValueObject):
    def __init__(self, value: str):
        self.__value = Rules.run(value)
        pass

    def get(self) -> str:
        return self.__value


class Rules(Rules):

    @staticmethod
    def run(value) -> bool:
        regex = r".{2,}"
        if not re.fullmatch(regex, value):
            raise CompanyNameExcepion("Company Name non valid length")
        return value


class CompanyNameExcepion(ValueObjectExcepion):
    pass
