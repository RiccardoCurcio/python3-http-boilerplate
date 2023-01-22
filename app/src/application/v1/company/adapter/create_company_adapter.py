from app.src.application.abc.adapter import Adapter
from aiohttp.web_request import Request
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.domain.valuesobjects.CompanyName import CompanyName
from app.src.domain.valuesobjects.VatNumber import VatNumber
from app.src.domain.valuesobjects.PhoneNumber import PhoneNumber
from app.src.domain.valuesobjects.Email import Email
from app.src.infrastructure.v1.company.entities import Company


class CreateCompanyAdapter(Adapter):

    def __init__(self, request: Request):
        self.__request: Request = request
        self.__company: Company = Company()

    async def adapt(self) -> Company:
        request = await self.__request.json()

        self.__company.id = ObjectId(request.get("id", None))
        self.__company.name = CompanyName(request.get("name", None))
        self.__company.vatNumber = VatNumber(request.get("vatNumber", None))
        self.__company.phones = [PhoneNumber(value) for value in request.get("phones", [])]
        self.__company.emails = [Email(value) for value in request.get("emails", [])]

        return self.__company
