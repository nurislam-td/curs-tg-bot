from sqlalchemy import select

from app.adapters.base_repo import AlchemyRepo
from app.services.entity.keyword import KeywordGroup
from app.services.abstract.repo import KeywordGroupRepo


class AlchemyKeywordGroupRepo(AlchemyRepo[KeywordGroup], KeywordGroupRepo):
    async def get_by_keyword_group_by_title(self, title: str) -> KeywordGroup:
        query = select(self._table).filter_by(title=title)
        return await self.fetch_one(query)
