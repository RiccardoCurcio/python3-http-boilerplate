import pytest
from app.src.infrastructure.v1.placeholder.gateways.create_placeholder_gateway import (
    CreatePaceholderGateway,
)

from app.src.infrastructure.v1.placeholder.repositories.create_placeholder_repository import CreatePlaceholderRepository

from app.src.infrastructure.v1.placeholder.entities import Placeholder


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_create_gateway_call")
    @pytest.mark.asyncio
    async def test_create_placeholder_from_mapper(self, placeholder):
        repository = CreatePlaceholderRepository(CreatePaceholderGateway())
        entity = await repository.create(placeholder)
        assert isinstance(entity, Placeholder) is True
