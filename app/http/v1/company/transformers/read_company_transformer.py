from app.http.abc.transformers import Tranformer
from app.src.v1.company.entities import Company


class ReadCompanyTranformer(Tranformer):

    @staticmethod
    def transform(data: Company) -> dict:
        return data.to_dict()
