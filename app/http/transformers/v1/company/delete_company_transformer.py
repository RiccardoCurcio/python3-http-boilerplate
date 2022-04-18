from app.http.transformers import Tranformer
from app.src.v1.entities.company import Company


class DeleteCompanyTranformer(Tranformer):

    @staticmethod
    def transform(data: Company) -> dict:
        return data
