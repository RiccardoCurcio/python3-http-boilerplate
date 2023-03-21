import pytest
from app.src.infrastructure.v1.placeholder.gateways.read_placeholder_gateway import (
    ReadPaceholderGateway,
)

from app.src.infrastructure.v1.placeholder.repositories.read_placeholder_repository import ReadPlaceholderRepository

from app.src.infrastructure.v1.placeholder.entities import Placeholder


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_read_gateway_call")
    @pytest.mark.asyncio
    async def test_read_placeholder_from_mapper(self, placeholder):
        repository = ReadPlaceholderRepository(ReadPaceholderGateway())
        entity = await repository.readById(placeholder)
        assert isinstance(entity, Placeholder) is True
