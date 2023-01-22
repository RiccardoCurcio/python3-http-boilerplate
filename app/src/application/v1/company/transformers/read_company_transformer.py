from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.company.entities import Company


class ReadCompanyTranformer(Tranformer):

    @staticmethod
    def transform(data: Company) -> dict:
        return data.to_dict()
