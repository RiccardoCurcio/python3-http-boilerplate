import pytest

from app.src.infrastructure.v1.placeholder.gateways.read_placeholder_gateway import (
    ReadPaceholderGateway,
)


class TestClass:
    @pytest.mark.asyncio
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_read__call")
    async def test_read_placeholder_gateway(self, placeholder):
        gateway = ReadPaceholderGateway()
        entity = await gateway.call(placeholder)
        assert type(entity) == dict
        assert entity.get("id") == "617c4d302bdaae79da0a6778"
