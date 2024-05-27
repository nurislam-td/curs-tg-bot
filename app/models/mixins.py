from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column


class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("(now() at time zone 'utc')"),
        index=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("(now() at time zone 'utc')"),
        onupdate=text("(now() at time zone 'utc')"),
    )
