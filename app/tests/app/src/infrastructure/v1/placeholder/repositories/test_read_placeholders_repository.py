import pytest
from app.src.infrastructure.v1.placeholder.gateways.read_placeholders_gateway import (
    ReadPaceholdersGateway,
)

from app.src.infrastructure.v1.placeholder.repositories.read_placeholders_repository import ReadPlaceholdersRepository

from app.src.infrastructure.v1.placeholder.entities import Placeholder


class TestClass:
    @pytest.mark.usefixtures("placeholder_query")
    @pytest.mark.usefixtures("mock_read_all_gateway_call")
    @pytest.mark.asyncio
    async def test_read_placeholder_from_mapper(self, placeholder_query):
        repository = ReadPlaceholdersRepository(ReadPaceholdersGateway())
        list_of_entity = await repository.read(placeholder_query)

        assert type(list_of_entity) == list

        for entity in list_of_entity:
            assert isinstance(entity, Placeholder) is True
