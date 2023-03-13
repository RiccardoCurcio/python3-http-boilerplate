from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.user.entities import User


class DeleteuserTranformer(Tranformer):

    @staticmethod
    def transform(data: User) -> dict:
        return data
