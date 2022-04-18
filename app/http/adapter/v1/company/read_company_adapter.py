from app.http.adapter import Adapter
from aiohttp.web_request import Request
from app.src.valuesobjects.ObjectId import ObjectId
from app.src.v1.entities.company import Company


class ReadCompanyAdapter(Adapter):

    def __init__(self, request: Request):
        self.__request: Request = request
        self.__company: Company = Company()

    async def adapt(self) -> Company:
        self.__company.id = ObjectId(self.__request.match_info.get('entity_id', None))

        return self.__company
