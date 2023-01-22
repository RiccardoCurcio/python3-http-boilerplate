from aiohttp.web import get, put, post, delete
from app.src.application.v1.company.controllers.create_company_controller import CreateCompanyController
from app.src.application.v1.company.controllers.read_companies_controller import ReadCompaniesController
from app.src.application.v1.company.controllers.read_company_controller import ReadCompanyController
from app.src.application.v1.company.controllers.update_company_controller import UpdateCompanyController
from app.src.application.v1.company.controllers.delete_company_controller import DeleteCompanyController

version = "v1"
path = "companies"

createCompanyController = CreateCompanyController()
readCompaniesController = ReadCompaniesController()
readCompanyController = ReadCompanyController()
updateCompanyController = UpdateCompanyController()
deleteCompanyController = DeleteCompanyController()

routes = [
    post(f"/{version}/{path}", createCompanyController.handle),
    get(f"/{version}/{path}/{{entity_id}}", readCompanyController.handle),
    get(f"/{version}/{path}", readCompaniesController.handle),
    put(f"/{version}/{path}/{{entity_id}}", updateCompanyController.handle),
    delete(f"/{version}/{path}/{{entity_id}}", deleteCompanyController.handle)
]
