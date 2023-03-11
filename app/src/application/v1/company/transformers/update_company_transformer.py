from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.company.entities import Company
from app.crypt import obfuscate


class UpdateCompanyTranformer(Tranformer):

    @staticmethod
    def transform(data: Company) -> dict:
        data = data.to_dict()
        data["id"] = obfuscate(data["id"])
        return data
