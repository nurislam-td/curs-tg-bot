from datetime import timedelta, datetime

from sqlalchemy import select, label, insert, Select

from app.adapters.base_repo import AlchemyRepo
from app.services.entity.reports import ReportDTO
from app.services.abstract.repo import ReportRepo
from app.models import keyword, TGUser, Chat


class AlchemyReportRepo(AlchemyRepo[ReportDTO], ReportRepo):
    keyword_table = keyword.Keyword.__table__
    keyword_map_table = keyword.KeywordMap.__table__
    keyword_group_table = keyword.KeywordGroup.__table__
    keyword_group_keyword_table = keyword.KeywordGroupKeywordMap.__table__
    tg_user_table = TGUser.__table__
    chat_table = Chat.__table__

    @classmethod
    def get_by_week(cls) -> Select:
        now = datetime.now()
        gt_time = now - timedelta(days=7)
        query = (
            select(
                label("chat_title", cls.chat_table.c.title),
                label("username", cls.tg_user_table.c.username),
                label("keyword", cls.keyword_table.c.keyword),
                label("groups", cls.keyword_group_table.c.title),
            )
            .select_from(cls.keyword_map_table)
            .join(
                cls.tg_user_table,
                cls.tg_user_table.c.id == cls.keyword_map_table.c.tg_user_id,
            )
            .join(
                cls.chat_table,
                cls.chat_table.c.id == cls.keyword_map_table.c.chat_id,
            )
            .join(
                cls.keyword_table,
                cls.keyword_table.c.id == cls.keyword_map_table.c.keyword_id,
            )
            .join(
                cls.keyword_group_keyword_table,
                cls.keyword_group_keyword_table.c.keyword_id == cls.keyword_table.c.id,
            )
            .join(
                cls.keyword_group_table,
                cls.keyword_group_table.c.id
                == cls.keyword_group_keyword_table.c.group_id,
            )
            .where(cls.keyword_map_table.c.created_at.between(gt_time, now))
        )
        return query

    async def create_for_week(self) -> None:
        select_query = self.get_by_week()
        query = insert(self._table).from_select(
            names=["chat_title", "username", "keyword", "groups"],
            select=select_query,
        )
        return await self.execute(query)
