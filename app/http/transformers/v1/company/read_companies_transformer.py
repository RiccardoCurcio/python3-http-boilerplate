from typing import List
from app.http.transformers import Tranformer
from app.src.v1.entities.company import Company


class ReadCompaniesTranformer(Tranformer):

    @staticmethod
    def transform(data: List[Company]) -> List[dict]:
        return list(map(lambda item: item.to_dict(), data))
