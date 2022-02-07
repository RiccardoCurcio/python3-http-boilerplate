from aiohttp.web import get, route
from controllers.v1.health_check_controller import HealthCheckController
from controllers.v1.resource_not_found_controller import ResourceNotFoundController
from routes.company import routes as company_routes

healthCheckController = HealthCheckController()
notFoundController = ResourceNotFoundController()

routes = company_routes + [
    get("/healthcheck", healthCheckController.handle),
    route("*", "/{tail:.*}", notFoundController.handle)
]
