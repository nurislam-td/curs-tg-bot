from app.adapters.chat import AlchemyChatRepo
from app.adapters.keyword_map_repo import AlchemyKeywordMapRepo
from app.adapters.report_repo import AlchemyReportRepo
from app.adapters.user import AlchemyTGUserRepo
from app.config.database import async_session_maker
from app.models import keyword, user, chat, reports
from app.adapters.keyword_repo import AlchemyKeywordRepo
from app.adapters.keyword_group_repo import AlchemyKeywordGroupRepo
from app.adapters.keyword_group_map_repo import AlchemyKeywordGroupMapRepo
from app.services.entity.chat import ChatDTO
from app.services.entity.keyword import (
    KeywordGroupDTO,
    KeywordDTO,
    KeywordGroupMapDTO,
    KeywordMapDTO,
)
from app.services.abstract.unit_of_work import UnitOfWork
from app.services.entity.reports import ReportDTO
from app.services.entity.user import TGUserDTO


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory=async_session_maker):
        self.session_factory = session_factory

    def __call__(self):
        return self

    async def __aenter__(self):
        self.session = self.session_factory()
        self.keyword = AlchemyKeywordRepo(
            session=self.session,
            schema=KeywordDTO,
            model=keyword.Keyword,
        )
        self.keyword_group = AlchemyKeywordGroupRepo(
            session=self.session,
            schema=KeywordGroupDTO,
            model=keyword.KeywordGroup,
        )
        self.keyword_group_map = AlchemyKeywordGroupMapRepo(
            session=self.session,
            schema=KeywordGroupMapDTO,
            model=keyword.KeywordGroupKeywordMap,
        )
        self.keyword_map = AlchemyKeywordMapRepo(
            session=self.session,
            schema=KeywordMapDTO,
            model=keyword.KeywordMap,
        )
        self.tg_user = AlchemyTGUserRepo(
            session=self.session, schema=TGUserDTO, model=user.TGUser
        )
        self.chat = AlchemyChatRepo(
            session=self.session, schema=ChatDTO, model=chat.Chat
        )
        self.report = AlchemyReportRepo(
            session=self.session, schema=ReportDTO, model=reports.KeywordMapReport
        )

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
