import pytest

from app.src.infrastructure.v1.placeholder.gateways.create_placeholder_gateway import (
    CreatePaceholderGateway,
)


class TestClass:
    @pytest.mark.asyncio
    @pytest.mark.usefixtures("placeholder")
    async def test_create_placeholder_gateway(self, placeholder):
        gateway = CreatePaceholderGateway()
        assert type(await gateway.call(placeholder)) == dict
