from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.mixins import TimeStampMixin, IntPKMixin, UUIDPKMixin

if TYPE_CHECKING:
    from app.models.user import TGUser
    from app.models.chat import Chat


class Keyword(UUIDPKMixin, Base):
    __tablename__ = "keyword"
    keyword: Mapped[str] = mapped_column(index=True, unique=True)
    keyword_map: Mapped[list["KeywordMap"]] = relationship(
        "KeywordMap", back_populates="keyword"
    )


class KeywordGroup(IntPKMixin, Base):
    __tablename__ = "keyword_group"
    title: Mapped[str] = mapped_column(String(length=50))
    description: Mapped[str | None] = mapped_column(String(length=255))
    is_active: Mapped[bool] = mapped_column(default=True)
    keyword_map = relationship("KeywordMap", back_populates="group")


class KeywordGroupKeywordMap(IntPKMixin, Base):
    __tablename__ = "keyword_group_keyword_map"
    group_id: Mapped[int] = mapped_column(
        ForeignKey("keyword_group.id", ondelete="CASCADE"), index=True
    )
    keyword_id: Mapped[int] = mapped_column(
        ForeignKey("keyword.id", ondelete="CASCADE"), index=True
    )


class KeywordMap(IntPKMixin, TimeStampMixin, Base):
    __tablename__ = "keyword_map"

    chat_id: Mapped[str] = mapped_column(ForeignKey("chat.id", ondelete="CASCADE"))
    chat: Mapped["Chat"] = relationship("Chat", back_populates="keyword_map")

    keyword_id: Mapped[int] = mapped_column(
        ForeignKey("keyword.id", ondelete="CASCADE"), index=True
    )
    keyword: Mapped["Keyword"] = relationship("Keyword", back_populates="keyword_map")

    tg_user_id: Mapped[str] = mapped_column(
        ForeignKey("tg_user.id", ondelete="CASCADE"),
        index=True,
    )
    tg_user: Mapped["TGUser"] = relationship("TGUser", back_populates="keyword_map")
