from aiohttp.web import middleware
from aiohttp.web_request import Request
from typing import Callable
from app.bootstrap.logger import logger


@middleware
async def example_middleware(request: Request, handler: Callable):
    logger.info('Example middleware')

    return await handler(request)
