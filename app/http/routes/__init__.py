import os
from aiohttp.web import get, route
from app.corss_origin import CorssOrigin
from app.http.abc.controllers.health_check_controller import HealthCheckController
from app.http.abc.controllers.resource_not_found_controller import ResourceNotFoundController
from app.http.routes.v1.company import routes as company_routes

class Routes:

    def __init__(self):
        self.__corssOrigin = CorssOrigin()
        self.__healthCheckController = HealthCheckController()
        self.__notFoundController = ResourceNotFoundController()

        self.__notFound = [
            route("*", "/{tail:.*}", self.__notFoundController.handle)
        ]

        self.__corssOriginRoute = [route("OPTIONS", "/{tail:.*}", self.__corssOrigin.handle)] if os.getenv("CORSS_ORIGIN_RESOLVE", False) in ("1", "True", "true", True) else []
        self.__routes = [
            get("/healthcheck", self.__healthCheckController.handle)
        ] + self.__corssOriginRoute + self.__notFound

    def add_routes(self) -> None:
        self.__routes = company_routes + self.__routes

    def get_routes(self) -> list:
        return self.__routes
