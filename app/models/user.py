from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class TGUser(Base):
    __tablename__ = "tg_user"

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    username: Mapped[str]
    keyword_map = relationship("KeywordMap", back_populates="tg_user")
