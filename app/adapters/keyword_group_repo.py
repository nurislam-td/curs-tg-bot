from sqlalchemy import select

from app.adapters.base_repo import AlchemyRepo
from app.services.entity.keyword import KeywordGroupDTO
from app.services.abstract.repo import KeywordGroupRepo


class AlchemyKeywordGroupRepo(AlchemyRepo[KeywordGroupDTO], KeywordGroupRepo):
    async def get_by_title(self, title: str) -> KeywordGroupDTO:
        query = select(self._table).filter_by(title=title)
        return await self.fetch_one(query)
