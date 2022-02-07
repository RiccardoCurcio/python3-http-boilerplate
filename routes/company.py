from aiohttp.web import get, put, post
from controllers.v1.company.create_company_controller import CreateCompanyController
from controllers.v1.company.read_companies_controller import ReadCompaniesController
from controllers.v1.company.read_company_controller import ReadCompanyController
from controllers.v1.company.update_company_controller import UpdateCompanyController

version = "v1"
path = "companies"

createCompanyController = CreateCompanyController()
readCompaniesController = ReadCompaniesController()
readCompanyController = ReadCompanyController()
updateCompanyController = UpdateCompanyController()

routes = [
    post(f"/{version}/{path}", createCompanyController.handle),
    get(f"/{version}/{path}/{{entity_id}}", readCompanyController.handle),
    get(f"/{version}/{path}", readCompaniesController.handle),
    put(f"/{version}/{path}/{{entity_id}}", updateCompanyController.handle)
]
