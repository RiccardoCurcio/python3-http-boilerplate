from aiohttp.web import get, put
from controllers.v1.company.read_companies_controller import ReadCompaniesController
from controllers.v1.company.read_company_controller import ReadCompanyController
from controllers.v1.company.update_company_controller import UpdateCompanyController

version = "v1"
path = "companies"

readCompaniesController = ReadCompaniesController()
readCompanyController = ReadCompanyController()
updateCompanyController = UpdateCompanyController()

routes = [
    get(f"/{version}/{path}/{{entity_id}}", readCompanyController.handle),
    get(f"/{version}/{path}", readCompaniesController.handle),
    put(f"/{version}/{path}/{{entity_id}}", updateCompanyController.handle)
]
