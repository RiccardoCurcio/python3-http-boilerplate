from app.src.application.abc.adapter import Adapter
from aiohttp.web_request import Request
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.infrastructure.v1.company.entities import Company
from app.crypt import deobfuscate


class DeleteCompanyAdapter(Adapter):

    def __init__(self, request: Request):
        self.__request: Request = request
        self.__company: Company = Company()

    async def adapt(self) -> Company:
        self.__company.id = ObjectId(deobfuscate(self.__request.match_info.get('entity_id', "")))

        return self.__company
