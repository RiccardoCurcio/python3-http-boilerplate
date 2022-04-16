from app.src.valuesobjects import ValueObject
import re


class CompanyName(ValueObject):
    def __init__(self, value: str):
        self.__value = Rules.run(value)
        pass

    def get(self) -> str:
        return self.__value


class Rules:

    @staticmethod
    def run(value) -> bool:
        regex = r".{2,}"
        if re.fullmatch(regex, value):
            return value
        else:
            raise CompanyNameExcepion("Company Name non valid length")


class CompanyNameExcepion(Exception):
    pass
