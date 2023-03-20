import pytest

from app.src.infrastructure.v1.placeholder.gateways.read_placeholders_gateway import (
    ReadPaceholdersGateway,
)


class TestClass:
    @pytest.mark.asyncio
    @pytest.mark.usefixtures("placeholder_query")
    @pytest.mark.usefixtures("mock_read_all__call")
    async def test_read_placeholder_gateway(self, placeholder_query):
        gateway = ReadPaceholdersGateway()
        list_of_entity = await gateway.call(placeholder_query)

        assert type(list_of_entity) == list

        assert list_of_entity[0].get("id") == "617c4d302bdaae79da0a6778"
        assert list_of_entity[1].get("id") == "617c4d302bdaae79da0a6779"
        assert list_of_entity[2].get("id") == "617c4d302bdaae79da0a6770"
