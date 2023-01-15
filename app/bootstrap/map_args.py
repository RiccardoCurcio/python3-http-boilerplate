import os

PERMITTED_ENV = ("ENV", "PREFIX", "PORT", "LOGGING_LEVEL", "SERVICE_NAME", "MEMCACHED_ENABLE")


def map_args(argv):
    try:
        param = next(argv)
        key, value = param.split("=")
        if key in PERMITTED_ENV:
            os.environ[key] = value
        map_args(argv)
    except:
        pass
