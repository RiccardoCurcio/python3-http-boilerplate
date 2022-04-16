from app.src.valuesobjects import ValueObject


class VatNumber(ValueObject):
    def __init__(self, value: str):
        self.__value = value
        pass

    def get(self) -> str:
        return self.__value
