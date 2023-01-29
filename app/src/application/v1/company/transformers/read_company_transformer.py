from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.company.entities import Company
from app.crypt import crypt


class ReadCompanyTranformer(Tranformer):
    @staticmethod
    def transform(data: Company) -> dict:
        data = data.to_dict()
        data["id"] = crypt(data["id"])
        return data
