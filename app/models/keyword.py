from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.mixins import TimeStampMixin

if TYPE_CHECKING:
    from app.models.user import User


class KeywordGroup(TimeStampMixin, Base):
    __tablename__ = "keyword_group"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(length=50))
    description: Mapped[str] = mapped_column(String(length=255))
    keywords: Mapped[list[str]] = mapped_column(ARRAY(String))
    is_active: Mapped[bool] = mapped_column(default=True)


class KeywordMap(Base, TimeStampMixin):
    __tablename__ = "keyword_map"

    map_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, index=True
    )
    chat_id: Mapped[str]

    group_id: Mapped[int] = mapped_column(
        ForeignKey("keyword_group.id", ondelete="CASCADE"), index=True
    )
    group: Mapped["KeywordGroup"] = relationship("KeywordGroup", back_populates="group")

    tg_user_id: Mapped[str] = mapped_column(
        ForeignKey("tg_user.user_id", ondelete="CASCADE"),
        index=True,
    )
    tg_user: Mapped["User"] = relationship("User", back_populates="keyword_map")
