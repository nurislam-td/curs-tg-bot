from typing import Any

from sqlalchemy.dialects.postgresql import insert

from app.adapters.base_repo import AlchemyRepo
from app.services.entity.keyword import KeywordDTO
from app.services.abstract.repo import KeywordRepo


class AlchemyKeywordRepo(AlchemyRepo[KeywordDTO], KeywordRepo):
    async def create_if_not_exists(
        self, keywords: list[dict[str, Any]]
    ) -> list[KeywordDTO] | None:
        query = (
            insert(self._table)
            .values(keywords)
            .on_conflict_do_nothing(index_elements=("keyword",))
        )
        return await self.execute(query)
