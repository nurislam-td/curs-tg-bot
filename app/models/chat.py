from typing import TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.models.base import Base

if TYPE_CHECKING:
    from app.models import KeywordMap


class Chat(Base):
    __tablename__ = "chat"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str | None]
    description: Mapped[str | None]
    keyword_map: Mapped[list["KeywordMap"]] = relationship(
        "KeywordMap", back_populates="chat"
    )
