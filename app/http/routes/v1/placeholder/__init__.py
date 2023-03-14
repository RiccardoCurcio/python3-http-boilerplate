from aiohttp.web import get, put, post, delete
from app.src.application.v1.placeholder.controllers.create_placeholder_controller import CreatePlaceholderController
from app.src.application.v1.placeholder.controllers.read_placeholders_controller import ReadPlaceholdersController
from app.src.application.v1.placeholder.controllers.read_placeholder_controller import ReadPlaceholderController
from app.src.application.v1.placeholder.controllers.update_placeholder_controller import UpdatePlaceholderController
from app.src.application.v1.placeholder.controllers.delete_placeholder_controller import DeletePlaceholderController

version = "v1"
path = "placeholders"

createPlaceholderController = CreatePlaceholderController()
readPlaceholdersController = ReadPlaceholdersController()
readPlaceholderController = ReadPlaceholderController()
updatePlaceholderController = UpdatePlaceholderController()
deletePlaceholderController = DeletePlaceholderController()

routes = [
    post(f"/{version}/{path}", createPlaceholderController.handle),
    get(f"/{version}/{path}/{{entity_id}}", readPlaceholderController.handle),
    get(f"/{version}/{path}", readPlaceholdersController.handle),
    put(f"/{version}/{path}/{{entity_id}}", updatePlaceholderController.handle),
    delete(f"/{version}/{path}/{{entity_id}}", deletePlaceholderController.handle)
]
