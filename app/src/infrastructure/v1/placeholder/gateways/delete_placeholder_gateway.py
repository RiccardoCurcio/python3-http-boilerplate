from app.src.domain.abc.gateway import DeleteGateway
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class DeletePaceholderGateway(DeleteGateway):
    async def call(self, data: Placeholder) -> dict:
        return {"placeholder": f"placeholder repo delete : {data.id.get()}"}
