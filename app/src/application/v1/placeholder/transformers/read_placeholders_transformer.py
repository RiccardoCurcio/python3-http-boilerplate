from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.placeholder.queries import Placeholder as PlaceholderQuery
from app.src.infrastructure.v1.placeholder.entities import Placeholder
from app.src.application.v1.placeholder.transformers.read_placeholder_transformer import ReadPlaceholderTranformer


class ReadPlaceholdersTranformer(Tranformer):

    @staticmethod
    def transform(data: list[Placeholder], query: PlaceholderQuery) -> dict:
        content: list[dict] = list(map(lambda item: ReadPlaceholderTranformer.transform(item), data))
        return {
            "pagination": {
                "skip": query.skip,
                "limit": query.limit,
                "count": len(content)
            },
            "content": content
        }