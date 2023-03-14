from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.placeholder.entities import Placeholder


class CreateplaceholderTranformer(Tranformer):

    @staticmethod
    def transform(data: Placeholder) -> dict:
        return data.to_dict()
