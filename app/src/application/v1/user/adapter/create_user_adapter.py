from app.src.application.abc.adapter import Adapter
from aiohttp.web_request import Request
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.domain.valuesobjects.Username import Username
from app.src.domain.valuesobjects.VatNumber import VatNumber
from app.src.domain.valuesobjects.PhoneNumber import PhoneNumber
from app.src.domain.valuesobjects.Email import Email
from app.src.infrastructure.v1.user.entities import User


class CreateuserAdapter(Adapter):

    def __init__(self, request: Request):
        self.__request: Request = request
        self.__user: User = User()

    async def adapt(self) -> User:
        request = await self.__request.json()

        self.__user.id = ObjectId(request.get("id")) if request.get("id", None) else None
        self.__user.name = Username(request.get("name", None))
        self.__user.vatNumber = VatNumber(request.get("vatNumber", None))
        self.__user.phones = [PhoneNumber(value) for value in request.get("phones", [])]
        self.__user.emails = [Email(value) for value in request.get("emails", [])]

        return self.__user
