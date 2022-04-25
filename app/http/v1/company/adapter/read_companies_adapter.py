# from typing import Union, List, Tuple
from app.http.abc.adapter import Adapter
from aiohttp.web_request import Request
from app.src.valuesobjects.ObjectId import ObjectId
from app.src.v1.company.queries import Company


class ReadCompaniesAdapter(Adapter):

    def __init__(self, request: Request):
        self.__request: Request = request
        self.__company_query: Company = Company()

    async def adapt(self) -> Company:
        # ObjectId(self.__request.match_info.get('entity_id', None))
        query = dict(self.__request.rel_url.query)
        self.__company_query.ids = [ObjectId(item) for item in query.get("ids", None).split(",")] if query.get("ids", None) else None  # Union[List[ObjectId], None] = None
        self.__company_query.searchKeys = [str(item) for item in query.get("searchkeys", None).split(",")] if query.get("searchkeys", None) else None  # : Union[List[str], None]
        self.__company_query.searchValues = [str(item) for item in query.get("searchvalues", None).split(",")] if query.get("searchvalues", None) else None  # : Union[List[str], None]
        self.__company_query.sort = int(query.get("sort", "1"))  # : int
        self.__company_query.sortKey = query.get("sortkey", "_id")  # : Union[str, None]
        self.__company_query.skip = int(query.get("skip", "0"))  # : int
        self.__company_query.limit = int(query.get("limit", "10"))  # : int
        self.__company_query.dateKeys = query.get("datekeys", None)  # : Union[List[str], None]
        self.__company_query.dateRanges = query.get("dateranges", None)  # : Union[List[Tuple], None]
        self.__company_query.createdAtRange = query.get("createdatrange", None)  # : Union[Tuple, None]
        self.__company_query.updatedAtRange = query.get("updatedatrange", None)  # : Union[Tuple, None]
        self.__company_query.deletedAtRange = query.get("deletedatrange", None)  # : Union[Tuple, None]
        return self.__company_query
