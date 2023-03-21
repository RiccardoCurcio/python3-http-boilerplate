import pytest
from app.src.infrastructure.v1.placeholder.gateways.delete_placeholder_gateway import (
    DeletePaceholderGateway,
)

from app.src.infrastructure.v1.placeholder.repositories.delete_placeholder_repository import DeletePlaceholderRepository


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_delete_gateway_call")
    @pytest.mark.asyncio
    async def test_delete_placeholder_from_mapper(self, placeholder):
        repository = DeletePlaceholderRepository(DeletePaceholderGateway())
        entity = await repository.delete(placeholder)
        assert type(entity) == dict
