from sqlalchemy import insert

from app.adapters.base_repo import AlchemyRepo
from app.services.entity.keyword import KeywordGroupMapDTO, KeywordGroupMapCreate
from app.services.abstract.repo import KeywordGroupMapRepo


class AlchemyKeywordGroupMapRepo(AlchemyRepo[KeywordGroupMapDTO], KeywordGroupMapRepo):
    async def create_keywords_group_maps(
        self, keyword_group_maps: list[KeywordGroupMapCreate]
    ) -> list[KeywordGroupMapDTO] | None:
        query = insert(self._table).values(
            [keyword_group_map.model_dump() for keyword_group_map in keyword_group_maps]
        )
        return await self.fetch_all(query=query)
