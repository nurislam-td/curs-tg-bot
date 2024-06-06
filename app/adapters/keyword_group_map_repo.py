from sqlalchemy import insert

from app.adapters.base_repo import AlchemyRepo
from app.services.entity.keyword import KeywordGroupMap
from app.services.abstract.repo import KeywordGroupMapRepo


class AlchemyKeywordGroupMapRepo(AlchemyRepo[KeywordGroupMap], KeywordGroupMapRepo):
    async def create_keywords_group_maps(
        self, keyword_group_maps: list[KeywordGroupMap]
    ) -> list[KeywordGroupMap] | None:
        query = insert(self._table).values(
            [keyword_group_map.as_dict() for keyword_group_map in keyword_group_maps]
        )
        return await self.fetch_all(query=query)
