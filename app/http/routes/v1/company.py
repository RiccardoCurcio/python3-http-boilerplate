from aiohttp.web import get, put, post, delete
from app.http.controllers.v1.company.create_company_controller import CreateCompanyController
from app.http.controllers.v1.company.read_companies_controller import ReadCompaniesController
from app.http.controllers.v1.company.read_company_controller import ReadCompanyController
from app.http.controllers.v1.company.update_company_controller import UpdateCompanyController
from app.http.controllers.v1.company.delete_company_controller import DeleteCompanyController

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
