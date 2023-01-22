import os
from aiohttp.web import get, route
from app.corss_origin import CorssOrigin
from app.src.application.abc.controllers.health_check_controller import HealthCheckController
from app.src.application.abc.controllers.resource_not_found_controller import ResourceNotFoundController

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
        # deve diventare dinamico
        from app.http.routes.v1.company import routes as company_routes

        self.__routes = company_routes + self.__routes

    def get_routes(self) -> list:
        return self.__routes
