import pytest
from app.src.infrastructure.v1.placeholder.gateways.update_placeholder_gateway import (
    UpdatePaceholderGateway,
)

from app.src.infrastructure.v1.placeholder.repositories.update_placeholder_repository import UpdatePlaceholderRepository

from app.src.infrastructure.v1.placeholder.entities import Placeholder


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_update_gateway_call")
    @pytest.mark.asyncio
    async def test_update_placeholder_from_mapper(self, placeholder):
        repository = UpdatePlaceholderRepository(UpdatePaceholderGateway())
        entity = await repository.update(placeholder)
        assert isinstance(entity, Placeholder) is True
