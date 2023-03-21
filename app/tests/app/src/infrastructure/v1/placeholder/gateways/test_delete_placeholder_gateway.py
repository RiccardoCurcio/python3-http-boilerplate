import pytest

from app.src.infrastructure.v1.placeholder.gateways.delete_placeholder_gateway import (
    DeletePaceholderGateway,
)


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_delete__call")
    @pytest.mark.asyncio
    async def test_delete_placeholder_gateway(self, placeholder):
        gateway = DeletePaceholderGateway()
        entity = await gateway.call(placeholder)

        assert type(entity) == dict
        assert entity.get("id") == "617c4d302bdaae79da0a6778"
