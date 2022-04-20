from typing import List
from app.http.transformers import Tranformer
from app.src.v1.queries.company import Company as CompanyQuery
from app.src.v1.entities.company import Company


class ReadCompaniesTranformer(Tranformer):

    @staticmethod
    def transform(data: List[Company], query: CompanyQuery) -> dict:
        content: List[dict] = list(map(lambda item: item.to_dict(), data))
        return {
            "pagination": {
                "skip": query.skip,
                "limit": query.limit,
                "count": len(content)
            },
            "content": content
        }
