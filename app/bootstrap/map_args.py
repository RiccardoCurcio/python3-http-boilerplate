import os
from app.bootstrap.logger import logger

PERMITTED_ENV = (
    "ENV",
    "PREFIX",
    "PORT",
    "LOGGING_LEVEL",
    "SERVICE_NAME",
    "MEMCACHED_ENABLE",
)


def map_args(argv):
    try:
        param = next(argv)
        key, value = param.split("=")
        if key in PERMITTED_ENV:
            os.environ[key] = value
        map_args(argv)
    except StopIteration:
        logger.info("Map args complete")
    except Exception:
        logger.error("map_args error: ", exc_info=True)
        pass
