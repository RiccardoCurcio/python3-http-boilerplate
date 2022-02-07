from aiohttp.web_request import Request

from controllers.v1 import Controller


class ResourceNotFoundController(Controller):
    async def handle(self, request: Request):
        return await self.error(request, "The requested resource does not exist", "Resource not found", 404)

    @property
    def schema(self) -> dict:
        return {}
