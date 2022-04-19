# from typing import Union, List, Tuple
from app.http.adapter import Adapter
from aiohttp.web_request import Request
# from app.src.valuesobjects.ObjectId import ObjectId
from app.src.v1.queries.company import Company


class ReadCompaniesAdapter(Adapter):

    def __init__(self, request: Request):
        self.__request: Request = request
        self.__company_query: Company = Company()

    async def adapt(self) -> Company:
        # ObjectId(self.__request.match_info.get('entity_id', None))
        self.__company_query.ids = None  # Union[List[ObjectId], None] = None
        self.__company_query.searchKeys = None  # : Union[List[str], None]
        self.__company_query.searchValues = None  # : Union[List[str], None]
        self.__company_query.sort = 1  # : int
        self.__company_query.sortKey = "_id"  # : Union[str, None]
        self.__company_query.skip = 0  # : int
        self.__company_query.limit = 10  # : int
        self.__company_query.dateKeys = None  # : Union[List[str], None]
        self.__company_query.dateRenges = None  # : Union[List[Tuple], None]
        self.__company_query.createdAtRange = None  # : Union[Tuple, None]
        self.__company_query.updatedAtRange = None  # : Union[Tuple, None]
        self.__company_query.deletedAtRange = None  # : Union[Tuple, None]

        return self.__company_query
