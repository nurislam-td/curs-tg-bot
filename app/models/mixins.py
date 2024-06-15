from datetime import datetime
from uuid import UUID

from sqlalchemy import text, types
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


class IntPKMixin:
    id: Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement=True)


class UUIDPKMixin:
    id: Mapped[UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()"),  # use what you have on your server
        index=True,
    )
