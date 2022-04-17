from typing import List, Union
from app.src.valuesobjects.ObjectId import ObjectId
from app.src.valuesobjects.CompanyName import CompanyName
from app.src.valuesobjects.VatNumber import VatNumber
from app.src.valuesobjects.PhoneNumber import PhoneNumber
from app.src.valuesobjects.Email import Email


class Company:
    def __init__(self):
        self.__id: ObjectId = None
        self.__name: CompanyName = None
        self.__vatNumber: Union[VatNumber, None] = None
        self.__phones: List[PhoneNumber] = []
        self.__emails: List[Email] = []
        pass

    def to_dict(self):
        return {
            "id": self.__id.get(),
            "name": self.__name.get(),
            "vatNumber": self.__vatNumber.get(),
            "phones": [value.get() for value in self.__phones],
            "emails": [value.get() for value in self.__emails]
        }

    @property
    def id(self) -> Union[ObjectId, None]:
        return self.__id

    @id.setter
    def id(self, id: ObjectId = None) -> None:
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