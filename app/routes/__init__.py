import os
from aiohttp.web import get, route
from app.corss_origin import CorssOrigin
from app.controllers.v1.health_check_controller import HealthCheckController
from app.controllers.v1.resource_not_found_controller import ResourceNotFoundController
from app.routes.company import routes as company_routes

corssOrigin = CorssOrigin()
healthCheckController = HealthCheckController()
notFoundController = ResourceNotFoundController()

notFound = [
    route("*", "/{tail:.*}", notFoundController.handle)
]

corssOriginRoute = [route("OPTIONS", "/{tail:.*}", corssOrigin.handle)] if os.getenv("CORSS_ORIGIN_RESOLVE", False) in ("1", "True", "true", True) else []

routes = company_routes + [
    get("/healthcheck", healthCheckController.handle)
] + corssOriginRoute + notFound
