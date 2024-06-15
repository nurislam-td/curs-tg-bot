from app.config.database import async_session_maker
from app.models import keyword
from app.adapters.keyword_repo import AlchemyKeywordRepo
from app.adapters.keyword_group_repo import AlchemyKeywordGroupRepo
from app.adapters.keyword_group_map_repo import AlchemyKeywordGroupMapRepo
from app.services.entity.keyword import (
    KeywordGroupCreate,
    KeywordCreate,
    KeywordGroupMapCreate,
)
from app.services.abstract.unit_of_work import UnitOfWork


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory=async_session_maker):
        self.session_factory = session_factory

    def __call__(self):
        return self

    async def __aenter__(self):
        self.session = self.session_factory()
        self.keyword = AlchemyKeywordRepo(
            session=self.session,
            schema=KeywordCreate,
            model=keyword.Keyword,
        )
        self.keyword_group = AlchemyKeywordGroupRepo(
            session=self.session,
            schema=KeywordGroupCreate,
            model=keyword.KeywordGroup,
        )
        self.keyword_group_map = AlchemyKeywordGroupMapRepo(
            session=self.session,
            schema=KeywordGroupMapCreate,
            model=keyword.KeywordGroupKeywordMap,
        )

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
