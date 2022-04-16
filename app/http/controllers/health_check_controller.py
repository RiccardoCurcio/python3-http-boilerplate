from aiohttp.web_request import Request
from app.http.controllers import Controller, error


class HealthCheckController(Controller):
    @property
    def schema(self) -> dict:
        return {}

    @error
    async def handle(self, request: Request):
        return self.response({}, 200)
