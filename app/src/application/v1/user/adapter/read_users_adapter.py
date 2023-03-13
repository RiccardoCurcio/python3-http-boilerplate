from app.src.application.abc.adapter import Adapter
from aiohttp.web_request import Request
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.infrastructure.v1.user.queries import User
from app.crypt import deobfuscate


class ReadUsersAdapter(Adapter):
    def __init__(self, request: Request):
        self.__request: Request = request
        self.__user_query: User = User()

    async def adapt(self) -> User:
        query = dict(self.__request.rel_url.query)
        self.__user_query.ids = (
            [ObjectId(deobfuscate(item)) for item in query["ids"].split(",")]
            if query.get("ids", None)
            else None
        )  # Union[list[ObjectId], None] = None
        self.__user_query.searchKeys = (
            [str(item) for item in query["searchkeys"].split(",")]
            if query.get("searchkeys", None)
            else None
        )  # : Union[list[str], None]
        self.__user_query.searchValues = (
            [str(item) for item in query["searchvalues"].split(",")]
            if query.get("searchvalues", None)
            else None
        )  # : Union[list[str], None]
        self.__user_query.sort = int(query.get("sort", "1"))  # : int
        self.__user_query.sortKey = query.get("sortkey", "_id")  # : Union[str, None]
        self.__user_query.skip = int(query.get("skip", "0"))  # : int
        self.__user_query.limit = int(query.get("limit", "10"))  # : int
        # self.__user_query.dateKeys = query.get("datekeys", None)  # : Union[list[str], None]
        # self.__user_query.dateRanges = query.get("dateranges", None)  # : Union[list[Tuple], None]
        # self.__user_query.createdAtRange = query.get("createdatrange", None)  # : Union[Tuple, None]
        # self.__user_query.updatedAtRange = query.get("updatedatrange", None)  # : Union[Tuple, None]
        # self.__user_query.deletedAtRange = query.get("deletedatrange", None)  # : Union[Tuple, None]
        return self.__user_query
