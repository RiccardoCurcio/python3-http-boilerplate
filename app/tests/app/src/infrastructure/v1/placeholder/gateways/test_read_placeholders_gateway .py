import pytest

from app.src.infrastructure.v1.placeholder.gateways.read_placeholders_gateway import (
    ReadPaceholdersGateway,
)


class TestClass:
    @pytest.mark.asyncio
    @pytest.mark.usefixtures("placeholder_query")
    async def test_read_placeholder_gateway(self, placeholder_query):
        gateway = ReadPaceholdersGateway()
        assert type(await gateway.call(placeholder_query)) == list
