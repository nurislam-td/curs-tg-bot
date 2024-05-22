from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class KeywordMap(Base):
    __tablename__ = 'keyword_map'

    map_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    chat_id: Mapped[str]
    user_id: Mapped[str] = mapped_column(ForeignKey('tg_user.user_id', ondelete='CASCADE'))
    tg_user: Mapped["User"] = relationship("User", back_populates="keyword_map")
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("(now() at time zone 'utc')")
    )
