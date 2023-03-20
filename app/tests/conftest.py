import pytest
from app.tests.app.src.infrastructure.v1.placeholder.entities import placeholder  # noqa: F401
from app.tests.app.src.infrastructure.v1.placeholder.queries import placeholder_query  # noqa: F401
from unittest.mock import AsyncMock


@pytest.fixture()
def mock_create__call(mocker):
    async_mock = AsyncMock()
    mocker.patch(
        "app.src.infrastructure.v1.placeholder.gateways.create_placeholder_gateway.CreatePaceholderGateway._CreatePaceholderGateway__call_service",
        side_effect=async_mock,
    )
    async_mock.return_value = {
        "id": "617c4d302bdaae79da0a6778",
        "name": "name_value",
        "vatNumber": "00000001",
        "phones": ["+39 349 0987654", "+39 349 4567890"],
        "emails": ["email1@email.com", "email2@email.com"],
    }
    return async_mock


@pytest.fixture()
def mock_read__call(mocker):
    async_mock = AsyncMock()
    mocker.patch(
        "app.src.infrastructure.v1.placeholder.gateways.read_placeholder_gateway.ReadPaceholderGateway._ReadPaceholderGateway__call_service",
        side_effect=async_mock,
    )
    async_mock.return_value = {
        "id": "617c4d302bdaae79da0a6778",
        "name": "name_value",
        "vatNumber": "00000001",
        "phones": ["+39 349 0987654", "+39 349 4567890"],
        "emails": ["email1@email.com", "email2@email.com"],
    }
    return async_mock


@pytest.fixture()
def mock_read_all__call(mocker):
    async_mock = AsyncMock()
    mocker.patch(
        "app.src.infrastructure.v1.placeholder.gateways.read_placeholders_gateway.ReadPaceholdersGateway._ReadPaceholdersGateway__call_service",
        side_effect=async_mock,
    )
    async_mock.return_value = [
        {
            "id": "617c4d302bdaae79da0a6778",
            "name": "name_value",
            "vatNumber": "00000001",
            "phones": ["+39 349 0987654", "+39 349 4567890"],
            "emails": ["email1@email.com", "email2@email.com"],
        },
        {
            "id": "617c4d302bdaae79da0a6779",
            "name": "name_value",
            "vatNumber": "00000001",
            "phones": ["+39 349 0987654", "+39 349 4567890"],
            "emails": ["email1@email.com", "email2@email.com"],
        },
        {
            "id": "617c4d302bdaae79da0a6770",
            "name": "name_value",
            "vatNumber": "00000001",
            "phones": ["+39 349 0987654", "+39 349 4567890"],
            "emails": ["email1@email.com", "email2@email.com"],
        }
    ]
    return async_mock
