from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.crypt import obfuscate


class ReadPlaceholderTranformer(Tranformer):
    @staticmethod
    def transform(data: Placeholder) -> dict:
        data = data.to_dict()
        data["id"] = obfuscate(data["id"])
        return data
