import pytest
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.services.delete_placeholder_service import (
    DeletePlaceholderService,
)
from app.src.infrastructure.v1.placeholder.repositories.delete_placeholder_repository import (
    DeletePlaceholderRepository,
)
from app.src.infrastructure.v1.placeholder.gateways.delete_placeholder_gateway import (
    DeletePaceholderGateway,
)


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_delete_gateway_call")
    @pytest.mark.asyncio
    async def test_service(self, placeholder):
        service = DeletePlaceholderService(
            repository=DeletePlaceholderRepository(DeletePaceholderGateway()),
            event=PlaceholderEvent("delete_placeholder_event"),
        )
        entity = await service.excute(data=placeholder)
        assert isinstance(entity, dict) is True
