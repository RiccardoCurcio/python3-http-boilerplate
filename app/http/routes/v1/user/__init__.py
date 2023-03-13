from aiohttp.web import get, put, post, delete
from app.src.application.v1.user.controllers.create_user_controller import CreateUserController
from app.src.application.v1.user.controllers.read_users_controller import ReadUsersController
from app.src.application.v1.user.controllers.read_user_controller import ReadUserController
from app.src.application.v1.user.controllers.update_user_controller import UpdateUserController
from app.src.application.v1.user.controllers.delete_user_controller import DeleteUserController

version = "v1"
path = "users"

createUserController = CreateUserController()
readUsersController = ReadUsersController()
readUserController = ReadUserController()
updateUserController = UpdateUserController()
deleteUserController = DeleteUserController()

routes = [
    post(f"/{version}/{path}", createUserController.handle),
    get(f"/{version}/{path}/{{entity_id}}", readUserController.handle),
    get(f"/{version}/{path}", readUsersController.handle),
    put(f"/{version}/{path}/{{entity_id}}", updateUserController.handle),
    delete(f"/{version}/{path}/{{entity_id}}", deleteUserController.handle)
]
