import os
import sys
from importlib import import_module
from aiohttp.web import get, route
from app.bootstrap.logger import logger
from app.corss_origin import CorssOrigin
from app.src.application.abc.controllers.health_check_controller import (
    HealthCheckController,
)
from app.src.application.abc.controllers.resource_not_found_controller import (
    ResourceNotFoundController,
)


class Routes:
    def __init__(self):
        self.__corssOrigin = CorssOrigin()
        self.__healthCheckController = HealthCheckController()
        self.__notFoundController = ResourceNotFoundController()

        self.__notFound = [route("*", "/{tail:.*}", self.__notFoundController.handle)]

        self.__corssOriginRoute = (
            [route("OPTIONS", "/{tail:.*}", self.__corssOrigin.handle)]
            if os.getenv("CORSS_ORIGIN_RESOLVE", False) in ("1", "True", "true", True)
            else []
        )
        self.__routes = (
            [get("/healthcheck", self.__healthCheckController.handle)]
            + self.__corssOriginRoute
            + self.__notFound
        )

    def add_routes(self) -> None:
        try:
            modules = []
            for routes_directory in list(
                filter(
                    lambda routes_directories: routes_directories[0] == "v",
                    os.listdir(os.path.dirname(__file__)),
                )
            ):

                modules.append(
                    list(
                        map(
                            lambda dirname: routes_directory + "." + dirname,
                            list(
                                filter(
                                    lambda mod: (mod[:2] != "__" and mod[-2:] != "__"),
                                    os.listdir(
                                        os.path.dirname(__file__)
                                        + "/"
                                        + routes_directory
                                    ),
                                )
                            ),
                        )
                    )
                )
            for submodules in modules:
                for module_name in submodules:
                    module = import_module("app.http.routes." + module_name)

                    self.__routes = module.routes + self.__routes
                    logger.info(f"routes Import  app.http.routes.{module_name} success")
        except Exception:
            logger.error("add_routes error: ", exc_info=True)
            sys.exit(1)

    def get_routes(self) -> list:
        return self.__routes
