import pytest
from typing import Tuple
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.infrastructure.v1.placeholder.queries import Placeholder


class MockQuery(Placeholder):
    def __init__(
        self,
        ids: list[ObjectId | None] = None,
        searchKeys: list[str | None] = None,
        searchValues: list[str | None] = None,
        sort: int = 1,
        sortKey: str | None = "_id",
        skip: int = 0,
        limit: int = 10,
        dateKeys: list[str | None] = None,
        dateRanges: list[Tuple | None] = None,
        createdAtRange: Tuple | None = None,
        updatedAtRange: Tuple | None = None,
        deletedAtRange: Tuple | None = None,
    ):
        self.ids = ids
        self.searchKeys = searchKeys
        self.searchValues = searchValues
        self.sort = sort
        self.sortKey = sortKey
        self.skip = skip
        self.limit = limit
        self.dateKeys = dateKeys
        self.dateRanges = dateRanges
        self.createdAtRange = createdAtRange
        self.updatedAtRange = updatedAtRange
        self.deletedAtRange = deletedAtRange


@pytest.fixture
def placeholder_query():
    return MockQuery()
