from datetime import date, timedelta

from sqlalchemy import insert, select

from app.adapters.base_repo import AlchemyRepo
from app.services.abstract.repo import KeywordMapRepo
from app.services.entity.keyword import KeywordMapDTO, KeywordMapCreate


class AlchemyKeywordMapRepo(AlchemyRepo[KeywordMapDTO], KeywordMapRepo):
    async def create_many(self, keyword_maps: list[KeywordMapCreate]) -> None:
        query = insert(self._table).values(
            [keyword_map.model_dump() for keyword_map in keyword_maps]
        )

        return await self.execute(query)

    async def get_by_week(self, *args, **kwargs) -> list[KeywordMapDTO]:
        today = date.today()
        gt_day = today - timedelta(days=7)
        query = select(self._table).where(self._model.created_at.between(gt_day, today))
        return await self.fetch_all(query)
