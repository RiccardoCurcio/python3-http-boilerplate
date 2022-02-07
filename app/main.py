import os
import sys

from aiohttp import web
from dotenv import load_dotenv, find_dotenv

from bootstrap.logger import logger
from routes import routes
from middlewares import example_middelware

load_dotenv(find_dotenv())

app = web.Application(middlewares=[example_middelware])
app.add_routes(routes)


if __name__ == '__main__':
    try:
        port = int(os.getenv('PORT'))
        logger.info(f'Starting server on port {port}...')
        web.run_app(app, port=port)
    except KeyboardInterrupt:
        logger.info('Stopping server...')
        sys.exit()
    except Exception as e:
        logger.error(f'There was an error while starting the server: {e}')
        sys.exit(1)
