import pytest
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.services.create_placeholder_service import (
    CreatePlaceholderService,
)
from app.src.infrastructure.v1.placeholder.repositories.create_placeholder_repository import (
    CreatePlaceholderRepository,
)
from app.src.infrastructure.v1.placeholder.gateways.create_placeholder_gateway import (
    CreatePaceholderGateway,
)
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_create_gateway_call")
    @pytest.mark.asyncio
    async def test_service(self, placeholder):
        service = CreatePlaceholderService(
            repository=CreatePlaceholderRepository(CreatePaceholderGateway()),
            event=PlaceholderEvent("create_placeholder_event"),
        )
        entity = await service.excute(data=placeholder)
        assert isinstance(entity, Placeholder) is True
