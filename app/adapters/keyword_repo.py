from app.adapters.base_repo import AlchemyRepo
from app.services.entity.keyword import Keyword
from app.services.abstract.repo import KeywordRepo


class AlchemyKeywordRepo(AlchemyRepo[Keyword], KeywordRepo):
    async def create_if_not_exists(self, keywords: list[str]) -> list[Keyword] | None:
        pass
