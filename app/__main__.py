import os
import sys

from aiohttp import web
from app.bootstrap.env import loaded
from app.bootstrap.logger import logger
from app.bootstrap.map_args import map_args
from app.http.routes import Routes
from app.middlewares import example_middleware


if __name__ == "__main__":
    try:
        logger.info(f"Env load {loaded}...")

        map_args(iter(sys.argv[1:]))
        port = int(os.getenv("PORT"))
        logger.info(f'Env {os.getenv("ENV")}')
        logger.info(f'Prefix {os.getenv("PREFIX")}')
        logger.info(f'Logging level {os.getenv("LOGGING_LEVEL")}')
        logger.info(f'Service name {os.getenv("SERVICE_NAME")}')
        app = web.Application(middlewares=[example_middleware])
        routes = Routes()
        routes.add_routes()
        app.add_routes(routes.get_routes())
        logger.info(f"Starting server on port {port}...")
        web.run_app(app, port=port)
    except KeyboardInterrupt:
        logger.info("Stopping server...")
        sys.exit(0)
    except Exception:
        logger.error("There was an error while starting the server: ", exc_info=True)
        sys.exit(1)
