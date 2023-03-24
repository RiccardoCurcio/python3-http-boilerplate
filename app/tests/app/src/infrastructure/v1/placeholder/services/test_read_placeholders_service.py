import pytest
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.services.read_placeholders_service import (
    ReadPlaceholdersService,
)
from app.src.infrastructure.v1.placeholder.repositories.read_placeholders_repository import (
    ReadPlaceholdersRepository,
)
from app.src.infrastructure.v1.placeholder.gateways.read_placeholders_gateway import (
    ReadPaceholdersGateway,
)
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class TestClass:
    @pytest.mark.usefixtures("placeholder_query")
    @pytest.mark.usefixtures("mock_read_gateway_call")
    @pytest.mark.asyncio
    async def test_service(self, placeholder_query):
        service = ReadPlaceholdersService(
            repository=ReadPlaceholdersRepository(ReadPaceholdersGateway()),
            event=PlaceholderEvent("read_placeholders_event"),
        )
        list_of_entity = await service.excute(query=placeholder_query)
        assert type(list_of_entity) == list

        for entity in list_of_entity:
            assert isinstance(entity, Placeholder) is True
