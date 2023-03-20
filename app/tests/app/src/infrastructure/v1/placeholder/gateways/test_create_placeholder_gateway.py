import pytest

from app.src.infrastructure.v1.placeholder.gateways.create_placeholder_gateway import (
    CreatePaceholderGateway,
)


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_create__call")
    @pytest.mark.asyncio
    async def test_create_placeholder_gateway(self, placeholder):
        gateway = CreatePaceholderGateway()
        entity = await gateway.call(placeholder)

        assert type(entity) == dict
        assert entity.get("id") == "617c4d302bdaae79da0a6778"
        assert entity.get("name") == "name_value"
