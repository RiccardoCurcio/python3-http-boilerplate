from aiohttp.web import middleware
from app.bootstrap.logger import logger


@middleware
async def example_middelware(request, handler):
    logger.info('Example middleware')

    return await handler(request)
