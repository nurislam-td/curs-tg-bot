from datetime import datetime

from pydantic import BaseModel


class ReportDTO(BaseModel):
    id: int
    keyword: str
    groups: str
    username: str
    chat_title: str | None
    created_at: datetime | None = datetime.now()


class ReportCreate(BaseModel):
    keyword: str
    groups: str
    username: str
    chat_title: str | None
    created_at: datetime | None = datetime.now()
