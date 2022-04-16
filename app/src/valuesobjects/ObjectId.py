from app.src.valuesobjects import ValueObject


class ObjectId(ValueObject):
    def __init__(self, value: str):
        self.__value = value
        pass

    def get(self) -> str:
        return self.__value
