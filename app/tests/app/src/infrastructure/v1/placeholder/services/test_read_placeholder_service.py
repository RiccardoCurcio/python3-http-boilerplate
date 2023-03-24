import pytest
from app.src.infrastructure.v1.placeholder.events import PlaceholderEvent
from app.src.infrastructure.v1.placeholder.services.read_placeholder_service import (
    ReadPlaceholderService,
)
from app.src.infrastructure.v1.placeholder.repositories.read_placeholder_repository import (
    ReadPlaceholderRepository,
)
from app.src.infrastructure.v1.placeholder.gateways.read_placeholder_gateway import (
    ReadPaceholderGateway,
)
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class TestClass:
    @pytest.mark.usefixtures("placeholder")
    @pytest.mark.usefixtures("mock_read_gateway_call")
    @pytest.mark.asyncio
    async def test_service(self, placeholder):
        service = ReadPlaceholderService(
            repository=ReadPlaceholderRepository(ReadPaceholderGateway()),
            event=PlaceholderEvent("read_placeholder_event"),
        )
        entity = await service.excute(data=placeholder)
        assert isinstance(entity, Placeholder) is True
