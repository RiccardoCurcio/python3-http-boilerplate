from app.http.transformers import Tranformer
from app.src.v1.entities.company import Company


class UpdateCompanyTranformer(Tranformer):

    @staticmethod
    def transform(data: Company) -> dict:
        return data.to_dict()
