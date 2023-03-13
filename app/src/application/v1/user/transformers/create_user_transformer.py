from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.user.entities import User


class CreateuserTranformer(Tranformer):

    @staticmethod
    def transform(data: User) -> dict:
        return data.to_dict()
