import pytest


@pytest.fixture()
def mock_create_gateway_call(mocker):
    return mocker.patch(
        "app.src.infrastructure.v1.placeholder.gateways.create_placeholder_gateway.CreatePaceholderGateway.call",
        return_value={
            "id": "617c4d302bdaae79da0a6778",
            "name": "name_value",
            "vatNumber": "00000001",
            "phones": ["+39 349 0987654", "+39 349 4567890"],
            "emails": ["email1@email.com", "email2@email.com"],
        },
    )


@pytest.fixture()
def mock_update_gateway_call(mocker):
    return mocker.patch(
        "app.src.infrastructure.v1.placeholder.gateways.update_placeholder_gateway.UpdatePaceholderGateway.call",
        return_value={
            "id": "617c4d302bdaae79da0a6778",
            "name": "name_value",
            "vatNumber": "00000001",
            "phones": ["+39 349 0987654", "+39 349 4567890"],
            "emails": ["email1@email.com", "email2@email.com"],
        },
    )


@pytest.fixture()
def mock_delete_gateway_call(mocker):
    return mocker.patch(
        "app.src.infrastructure.v1.placeholder.gateways.delete_placeholder_gateway.DeletePaceholderGateway.call",
        return_value={
            "id": "617c4d302bdaae79da0a6778"
        },
    )


@pytest.fixture()
def mock_read_gateway_call(mocker):
    return mocker.patch(
        "app.src.infrastructure.v1.placeholder.gateways.read_placeholder_gateway.ReadPaceholderGateway.call",
        return_value={
            "id": "617c4d302bdaae79da0a6778",
            "name": "name_value",
            "vatNumber": "00000001",
            "phones": ["+39 349 0987654", "+39 349 4567890"],
            "emails": ["email1@email.com", "email2@email.com"],
        },
    )


@pytest.fixture()
def mock_read_all_gateway_call(mocker):
    return mocker.patch(
        "app.src.infrastructure.v1.placeholder.gateways.read_placeholders_gateway.ReadPaceholdersGateway.call",
        return_value=[
            {
                "id": "617c4d302bdaae79da0a6771",
                "name": "name_value",
                "vatNumber": "00000001",
                "phones": ["+39 349 0987654", "+39 349 4567890"],
                "emails": ["email1@email.com", "email2@email.com"],
            },
            {
                "id": "617c4d302bdaae79da0a6772",
                "name": "name_value",
                "vatNumber": "00000001",
                "phones": ["+39 349 0987654", "+39 349 4567890"],
                "emails": ["email1@email.com", "email2@email.com"],
            },
            {
                "id": "617c4d302bdaae79da0a6773",
                "name": "name_value",
                "vatNumber": "00000001",
                "phones": ["+39 349 0987654", "+39 349 4567890"],
                "emails": ["email1@email.com", "email2@email.com"],
            }
        ],
    )
