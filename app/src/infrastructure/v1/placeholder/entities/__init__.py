from typing import Union
from app.src.domain.abc.entity import Entity
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.domain.valuesobjects.Username import Username
from app.src.domain.valuesobjects.VatNumber import VatNumber
from app.src.domain.valuesobjects.PhoneNumber import PhoneNumber
from app.src.domain.valuesobjects.Email import Email


class Placeholder(Entity):
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__vatNumber = None
        self.__phones = []
        self.__emails = []
        pass

    def to_dict(self) -> dict:
        return {
            "id": self.__id.get() if self.__id else None,
            "name": self.__name.get() if self.__name else None,
            "vatNumber": self.__vatNumber.get() if self.__vatNumber else None,
            "phones": [value.get() for value in self.__phones] if self.__phones else [],
            "emails": [value.get() for value in self.__emails] if self.__emails else []
        }

    @property
    def id(self) -> Union[ObjectId, None]:
        return self.__id

    @id.setter
    def id(self, id: Union[ObjectId, None] = None) -> None:
        self.__id = id
        return None

    @property
    def name(self) -> Username:
        return self.__name

    @name.setter
    def name(self, name: Username) -> None:
        self.__name = name
        return None

    @property
    def vatNumber(self) -> Union[VatNumber, None]:
        return self.__vatNumber

    @vatNumber.setter
    def vatNumber(self, vatNumber: Union[VatNumber, None] = None) -> None:
        self.__vatNumber = vatNumber
        return None

    @property
    def phones(self) -> list[PhoneNumber]:
        return self.__phones

    @phones.setter
    def phones(self, phoneNumbers: list[PhoneNumber] = []) -> None:
        self.__phones = phoneNumbers
        return None

    @property
    def emails(self) -> list[Email]:
        return self.__emails

    @emails.setter
    def emails(self, emails: list[Email] = []) -> None:
        self.__emails = emails
        return None
