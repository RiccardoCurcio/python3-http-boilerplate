from app.src.domain.valuesobjects import ValueObject


class PhoneNumber(ValueObject):
    def __init__(self, value: str):
        self.__value = value
        pass

    def get(self) -> str:
        return self.__value
