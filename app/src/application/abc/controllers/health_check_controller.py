from aiohttp.web_request import Request
from app.src.application.abc.controllers import Controller, error


class HealthCheckController(Controller):
    @property
    def schema(self) -> dict:
        return {}

    @error
    async def handle(self, request: Request):
        return self.response({}, 200)
