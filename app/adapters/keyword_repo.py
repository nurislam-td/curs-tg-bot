from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from app.adapters.base_repo import AlchemyRepo
from app.services.entity.keyword import KeywordDTO, KeywordCreate
from app.services.abstract.repo import KeywordRepo


class AlchemyKeywordRepo(AlchemyRepo[KeywordDTO], KeywordRepo):
    async def create_if_not_exists(self, keywords: list[KeywordCreate]) -> None:
        query = (
            insert(self._table)
            .values([keyword.model_dump() for keyword in keywords])
            .on_conflict_do_nothing(index_elements=("keyword",))
        )
        return await self.execute(query)

    async def get_by_keywords(self, keywords: set[str]) -> list[KeywordDTO] | None:
        query = select(self._table).where(self._model.keyword.in_(keywords))
        return await self.fetch_all(query)
