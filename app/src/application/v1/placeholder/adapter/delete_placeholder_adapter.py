from app.src.application.abc.adapter import Adapter
from aiohttp.web_request import Request
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.crypt import deobfuscate


class DeleteplaceholderAdapter(Adapter):

    def __init__(self, request: Request):
        self.__request: Request = request
        self.__placeholder: Placeholder = Placeholder()

    async def adapt(self) -> Placeholder:
        self.__placeholder.id = ObjectId(deobfuscate(self.__request.match_info.get('entity_id', "")))

        return self.__placeholder
