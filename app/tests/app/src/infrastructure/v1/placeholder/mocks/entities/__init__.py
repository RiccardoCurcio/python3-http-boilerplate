import pytest
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.domain.valuesobjects.ObjectId import ObjectId
from app.src.domain.valuesobjects.Username import Username
from app.src.domain.valuesobjects.VatNumber import VatNumber
from app.src.domain.valuesobjects.Email import Email
from app.src.domain.valuesobjects.PhoneNumber import PhoneNumber


class MockEntity(Placeholder):
    def __init__(
        self,
        id: str,
        name: str,
        vatNumber: str,
        emails: list[str | None],
        phones: list[str | None],
    ):
        self.id = ObjectId(id)
        self.name = Username(name)
        self.vatNumber = VatNumber(vatNumber)
        self.emails = list(map(lambda item: Email(item), emails))
        self.phones = list(map(lambda item: PhoneNumber(item), phones))


@pytest.fixture
def placeholder():
    return MockEntity(
        id="617c4d302bdaae79da0a6778",
        name="nameone",
        vatNumber="0000",
        emails=["test1@test.com", "test2@test.com"],
        phones=["+39 349 2222222", "+39 349 1111111"],
    )


@pytest.fixture
def placeholder_list():
    return [
        MockEntity(
            id="617c4d302bdaae79da0a6778",
            name="nameone",
            vatNumber="0000",
            emails=["test1@test.com", "test2@test.com"],
            phones=["+39 349 2222222", "+39 349 1111111"],
        ),
        MockEntity(
            id="617c4d302bdaae79da0a6779",
            name="nametwo",
            vatNumber="0000",
            emails=["test1@test.com", "test2@test.com"],
            phones=["+39 349 2222222", "+39 349 1111111"],
        ),
    ]
