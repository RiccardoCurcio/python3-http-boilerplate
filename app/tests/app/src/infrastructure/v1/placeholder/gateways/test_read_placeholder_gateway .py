import pytest

from app.src.infrastructure.v1.placeholder.gateways.read_placeholder_gateway import (
    ReadPaceholderGateway,
)


class TestClass:
    @pytest.mark.asyncio
    @pytest.mark.usefixtures("placeholder")
    async def test_read_placeholder_gateway(self, placeholder):
        gateway = ReadPaceholderGateway()
        assert type(await gateway.call(placeholder)) == dict
