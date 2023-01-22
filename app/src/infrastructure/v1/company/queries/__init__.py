from typing import List, Tuple, Union
from app.src.domain.abc.query import Query
from app.src.domain.valuesobjects.ObjectId import ObjectId


class Company(Query):
    def __init__(self):
        self.__ids: Union[List[ObjectId], None] = None
        self.__searchKeys: Union[List[str], None] = None
        self.__searchValues: Union[List[str], None] = None
        self.__sort: int = 1
        self.__sortKey: Union[str, None] = "_id"
        self.__skip: int = 0
        self.__limit: int = 10
        self.__dateKeys: Union[List[str], None] = None
        self.__dateRanges: Union[List[Tuple], None] = None
        self.__createdAtRange: Union[Tuple, None] = None
        self.__updatedAtRange: Union[Tuple, None] = None
        self.__deletedAtRange: Union[Tuple, None] = None
        pass

    def to_dict(self) -> dict:
        return {
            "ids": [
                value.get() for value in self.__ids
            ] if self.__ids else self.__ids
        }

    @property
    def ids(self) -> Union[List[ObjectId], None]:
        return self.__ids

    @ids.setter
    def ids(self, ids: Union[List[ObjectId], None] = None) -> None:
        self.__ids = ids
        return None

    @property
    def searchKeys(self) -> Union[List[str], None]:
        return self.__searchKeys

    @searchKeys.setter
    def searchKeys(self, searchKeys: Union[List[str], None] = None) -> None:
        self.__searchKeys = searchKeys
        return None

    @property
    def searchValues(self) -> Union[List[str], None]:
        return self.__searchValues

    @searchValues.setter
    def searchValues(self, searchValues: Union[List[str], None] = None) -> None:
        self.__searchValues = searchValues
        return None

    @property
    def sort(self) -> int:
        return self.__sort

    @sort.setter
    def sort(self, sort: int = 1) -> None:
        self.__sort = sort
        return None

    @property
    def sortKey(self) -> Union[str, None]:
        return self.__sortKey

    @sortKey.setter
    def sortKey(self, sortKey: Union[str, None] = "_id") -> None:
        self.__sortKey = sortKey
        return None

    @property
    def skip(self) -> int:
        return self.__skip

    @skip.setter
    def skip(self, skip: int = 1) -> None:
        self.__skip = skip
        return None

    @property
    def limit(self) -> int:
        return self.__limit

    @limit.setter
    def limit(self, limit: int = 1) -> None:
        self.__limit = limit
        return None

    @property
    def dateKeys(self) -> Union[List[str], None]:
        return self.__dateKeys

    @dateKeys.setter
    def dateKeys(self, dateKeys: Union[List[str], None] = None) -> None:
        self.__dateKeys = dateKeys
        return None

    @property
    def dateRanges(self) -> Union[List[Tuple], None]:
        return self.__dateRanges

    @dateRanges.setter
    def dateRanges(self, dateRanges: Union[List[Tuple], None] = None) -> None:
        self.__dateRanges = dateRanges
        return None

    @property
    def createdAtRange(self) -> Union[Tuple, None]:
        return self.__createdAtRange

    @createdAtRange.setter
    def createdAtRange(self, createdAtRange: Union[Tuple, None] = None) -> None:
        self.__createdAtRange = createdAtRange
        return None

    @property
    def updatedAtRange(self) -> Union[Tuple, None]:
        return self.__updatedAtRange

    @updatedAtRange.setter
    def updatedAtRange(self, updatedAtRange: Union[Tuple, None] = None) -> None:
        self.__updatedAtRange = updatedAtRange
        return None

    @property
    def deletedAtRange(self) -> Union[Tuple, None]:
        return self.__deletedAtRange

    @deletedAtRange.setter
    def deletedAtRange(self, deletedAtRange: Union[Tuple, None] = None) -> None:
        self.__deletedAtRange = deletedAtRange
        return None
