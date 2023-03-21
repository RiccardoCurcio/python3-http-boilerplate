import pytest
from app.src.infrastructure.v1.placeholder.gateways.create_placeholder_gateway import (
    CreatePaceholderGateway,
)
from app.src.infrastructure.v1.placeholder.gateways.update_placeholder_gateway import (
    UpdatePaceholderGateway,
)
from app.src.infrastructure.v1.placeholder.gateways.read_placeholder_gateway import (
    ReadPaceholderGateway,
)
from app.src.infrastructure.v1.placeholder.gateways.read_placeholders_gateway import (
    ReadPaceholdersGateway,
)
from app.src.infrastructure.v1.placeholder.mapper import Mapper
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_create_gateway_call")
    @pytest.mark.asyncio
    async def test_create_placeholder_from_mapper(self, placeholder):
        gateway = CreatePaceholderGateway()
        entity = await gateway.call(placeholder)
        assert isinstance(Mapper.map(entity), Placeholder) is True

    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_update_gateway_call")
    @pytest.mark.asyncio
    async def test_update_placeholder_from_mapper(self, placeholder):
        gateway = UpdatePaceholderGateway()
        entity = await gateway.call(placeholder)
        assert isinstance(Mapper.map(entity), Placeholder) is True

    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_read_gateway_call")
    @pytest.mark.asyncio
    async def test_read_placeholder_from_mapper(self, placeholder):
        gateway = ReadPaceholderGateway()
        entity = await gateway.call(placeholder)
        assert isinstance(Mapper.map(entity), Placeholder) is True

    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_read_all_gateway_call")
    @pytest.mark.asyncio
    async def test_read_placeholders_from_mapper(self, placeholder):
        gateway = ReadPaceholdersGateway()
        entities = await gateway.call(placeholder)

        assert type(entities) == list

        for entity in Mapper.map_list(entities):
            assert isinstance(entity, Placeholder) is True
