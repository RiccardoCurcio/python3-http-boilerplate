from aiohttp.web import get, route
from app.controllers.v1.health_check_controller import HealthCheckController
from app.controllers.v1.resource_not_found_controller import ResourceNotFoundController
from app.routes.company import routes as company_routes

healthCheckController = HealthCheckController()
notFoundController = ResourceNotFoundController()

routes = company_routes + [
    get("/healthcheck", healthCheckController.handle),
    route("*", "/{tail:.*}", notFoundController.handle)
]
