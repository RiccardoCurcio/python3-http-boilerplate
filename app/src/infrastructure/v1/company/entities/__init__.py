from typing import List, Union
from app.src.domain.abc.entity import Entity
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.domain.valuesobjects.CompanyName import CompanyName
from app.src.domain.valuesobjects.VatNumber import VatNumber
from app.src.domain.valuesobjects.PhoneNumber import PhoneNumber
from app.src.domain.valuesobjects.Email import Email


class Company(Entity):
    def __init__(self):
        self.__id: Union[ObjectId, None] = None
        self.__name: CompanyName = None
        self.__vatNumber: Union[VatNumber, None] = None
        self.__phones: List[PhoneNumber] = []
        self.__emails: List[Email] = []
        pass

    def to_dict(self) -> dict:
        return {
            "id": self.__id.get() if self.__id else None,
            "name": self.__name.get() if self.__name else None,
            "vatNumber": self.__vatNumber.get() if self.__vatNumber else None,
            "phones": [value.get() for value in self.__phones],
            "emails": [value.get() for value in self.__emails]
        }

    @property
    def id(self) -> Union[ObjectId, None]:
        return self.__id

    @id.setter
    def id(self, id: Union[ObjectId, None] = None) -> None:
        self.__id = id
        return None

    @property
    def name(self) -> CompanyName:
        return self.__name

    @name.setter
    def name(self, name: CompanyName) -> None:
        self.__name = name
        return None

    @property
    def vatNumber(self) -> Union[VatNumber, None]:
        return self.__vatNumber

    @vatNumber.setter
    def vatNumber(self, vatNumber: VatNumber = None) -> None:
        self.__vatNumber = vatNumber
        return None

    @property
    def phones(self) -> List[PhoneNumber]:
        return self.__phones

    @phones.setter
    def phones(self, phoneNumbers: List[PhoneNumber] = []) -> None:
        self.__phones = phoneNumbers
        return None

    @property
    def emails(self) -> List[Email]:
        return self.__emails

    @emails.setter
    def emails(self, emails: List[Email] = []) -> None:
        self.__emails = emails
        return None
