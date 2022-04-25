from app.http.abc.adapter import Adapter
from aiohttp.web_request import Request
from app.src.valuesobjects.ObjectId import ObjectId
from app.src.v1.company.entities import Company
from app.src.valuesobjects.CompanyName import CompanyName
from app.src.valuesobjects.VatNumber import VatNumber
from app.src.valuesobjects.PhoneNumber import PhoneNumber
from app.src.valuesobjects.Email import Email


class UpdateCompanyAdapter(Adapter):

    def __init__(self, request: Request):
        self.__request: Request = request
        self.__company: Company = Company()

    async def adapt(self) -> Company:
        request = await self.__request.json()
        self.__company.id = ObjectId(self.__request.match_info.get('entity_id', None))
        self.__company.name = CompanyName(request.get("name", None))
        self.__company.vatNumber = VatNumber(request.get("vatNumber", None))
        self.__company.phones = [PhoneNumber(value) for value in request.get("phones", [])]
        self.__company.emails = [Email(value) for value in request.get("emails", [])]

        return self.__company
