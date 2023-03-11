from typing import List
from app.src.application.abc.transformers import Tranformer
from app.src.infrastructure.v1.company.queries import Company as CompanyQuery
from app.src.infrastructure.v1.company.entities import Company
from app.src.application.v1.company.transformers.read_company_transformer import ReadCompanyTranformer


class ReadCompaniesTranformer(Tranformer):

    @staticmethod
    def transform(data: List[Company], query: CompanyQuery) -> dict:
        content: List[dict] = list(map(lambda item: ReadCompanyTranformer.transform(item.to_dict()), data))
        return {
            "pagination": {
                "skip": query.skip,
                "limit": query.limit,
                "count": len(content)
            },
            "content": content
        }