from app.src.infrastructure.v1.placeholder.entities import Placeholder

from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.domain.valuesobjects.Username import Username
from app.src.domain.valuesobjects.VatNumber import VatNumber
from app.src.domain.valuesobjects.PhoneNumber import PhoneNumber
from app.src.domain.valuesobjects.Email import Email


class Mapper:
    @staticmethod
    def map(data_dict: dict) -> Placeholder:
        placeholder = Placeholder()
        placeholder.id = (
            ObjectId(data_dict.get("id")) if data_dict.get("id", None) else None
        )
        placeholder.name = Username(data_dict.get("name", None))
        placeholder.vatNumber = VatNumber(data_dict.get("vatNumber", None))
        placeholder.phones = [
            PhoneNumber(value) for value in data_dict.get("phones", [])
        ]
        placeholder.emails = [Email(value) for value in data_dict.get("emails", [])]
        return placeholder

    @staticmethod
    def map_list(data_list: list) -> list[Placeholder]:
        return list(map(lambda item: Mapper.map(item), data_list))
