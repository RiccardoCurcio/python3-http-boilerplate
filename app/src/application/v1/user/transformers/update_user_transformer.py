from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.user.entities import User
from app.crypt import obfuscate


class UpdateuserTranformer(Tranformer):

    @staticmethod
    def transform(data: User) -> dict:
        data = data.to_dict()
        data["id"] = obfuscate(data["id"])
        return data
