from aiohttp.web_request import Request
from aiohttp import web
import os
from app.bootstrap.logger import logger


class CorssOrigin:
    def __init__(self) -> None:
        pass

    async def handle(self, request: Request):
        logger.info('Corss-origin resolver')

        return web.json_response(
            data=None,
            status=204,
            content_type="application/vnd.api+json",
            headers={
                "Access-Control-Allow-Origin": os.getenv("ALLOW_ORIGIN", ""),
                "Access-Control-Allow-Methods": os.getenv("ALLOW_METHODS", ""),
                "Access-Control-Allow-Headers": os.getenv("ALLOW_HEADERS", ""),
                "Access-Control-Max-Age": os.getenv("MAX_AGE", "86400"),
                "Server": os.getenv("SERVICE_NAME", "PY3-http-boilerplate")
            }
        )
