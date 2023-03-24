import pytest
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.services.update_placeholder_service import (
    UpdatePlaceholderService,
)
from app.src.infrastructure.v1.placeholder.repositories.update_placeholder_repository import (
    UpdatePlaceholderRepository,
)
from app.src.infrastructure.v1.placeholder.gateways.update_placeholder_gateway import (
    UpdatePaceholderGateway,
)
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_update_gateway_call")
    @pytest.mark.asyncio
    async def test_service(self, placeholder):
        service = UpdatePlaceholderService(
            repository=UpdatePlaceholderRepository(UpdatePaceholderGateway()),
            event=PlaceholderEvent("update_placeholder_event"),
        )
        entity = await service.excute(data=placeholder)
        assert isinstance(entity, Placeholder) is True
