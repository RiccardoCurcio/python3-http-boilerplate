from app.src.application.abc.adapter import Adapter
from aiohttp.web_request import Request
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.infrastructure.v1.user.entities import User
from app.crypt import deobfuscate


class ReaduserAdapter(Adapter):
    def __init__(self, request: Request):
        self.__request: Request = request
        self.__user: User = User()

    async def adapt(self) -> User:
        self.__user.id = ObjectId(deobfuscate(self.__request.match_info.get("entity_id", "")))

        return self.__user
