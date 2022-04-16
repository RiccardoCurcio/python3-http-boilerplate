import os
import sys

from aiohttp import web
from app.bootstrap.env import loaded
from app.bootstrap.logger import logger
from app.http.routes import routes
from app.middlewares import example_middelware


app = web.Application(middlewares=[example_middelware])
app.add_routes(routes)


if __name__ == '__main__':
    try:
        port = int(os.getenv('PORT'))
        logger.info(f'Env load {loaded}...')
        logger.info(f'Starting server on port {port}...')
        web.run_app(app, port=port)
    except KeyboardInterrupt:
        logger.info('Stopping server...')
        sys.exit(0)
    except Exception as e:
        logger.error(f'There was an error while starting the server: {e}')
        sys.exit(1)
