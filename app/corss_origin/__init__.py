from aiohttp.web_request import Request
from aiohttp import web
import os
from app.bootstrap.logger import logger


corss_headers = {
    "access-control-allow-credentials": os.getenv("ALLOW_CREDENTIALS", "true"),
    "access-control-allow-origin": os.getenv("ALLOW_ORIGIN", "*"),
    "access-control-allow-methods": os.getenv("ALLOW_METHODS", "*"),
    "access-control-allow-headers": os.getenv("ALLOW_HEADERS", "*"),
    "access-control-max-age": os.getenv("MAX_AGE", "0"),
    "access-control-expose-headers": " ",
    "Server": os.getenv("SERVICE_NAME", "PY3-http-boilerplate"),
    "vary": os.getenv("VARY", "Origin"),
    "cache-controll": os.getenv("CACHE_CONTROLL", "private, must-revalidate")
}


class CorssOrigin:
    def __init__(self) -> None:
        pass

    async def handle(self, request: Request):
        logger.info('Corss-origin resolver')

        return web.json_response(
            data=None,
            status=204,
            content_type="application/vnd.api+json",
            headers=corss_headers
        )
