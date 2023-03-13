from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.user.queries import User as UserQuery
from app.src.infrastructure.v1.user.entities import User
from app.src.application.v1.user.transformers.read_user_transformer import ReadUserTranformer


class ReadUsersTranformer(Tranformer):

    @staticmethod
    def transform(data: list[User], query: UserQuery) -> dict:
        content: list[dict] = list(map(lambda item: ReadUserTranformer.transform(item.to_dict()), data))
        return {
            "pagination": {
                "skip": query.skip,
                "limit": query.limit,
                "count": len(content)
            },
            "content": content
        }