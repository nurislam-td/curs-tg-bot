from sqlalchemy.orm import Mapped

from app.models.base import Base
from app.models.mixins import IntPKMixin, TimeStampMixin


class KeywordMapReport(IntPKMixin, TimeStampMixin, Base):
    __tablename__ = "keyword_map_report"

    keyword: Mapped[str | None]
    groups: Mapped[str | None]
    username: Mapped[str | None]
    chat_title: Mapped[str | None]
