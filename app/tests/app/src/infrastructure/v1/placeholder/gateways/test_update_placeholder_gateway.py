import pytest

from app.src.infrastructure.v1.placeholder.gateways.update_placeholder_gateway import (
    UpdatePaceholderGateway,
)


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_update__call")
    @pytest.mark.asyncio
    async def test_update_placeholder_gateway(self, placeholder):
        gateway = UpdatePaceholderGateway()
        entity = await gateway.call(placeholder)

        assert type(entity) == dict
        assert entity.get("id") == "617c4d302bdaae79da0a6778"
        assert entity.get("name") == "name_value"
