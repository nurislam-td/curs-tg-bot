import dataclasses

from app.services.base import Base


@dataclasses.dataclass
class KeywordGroup(Base):
    id: int
    title: str
    description: str
    is_active: bool


@dataclasses.dataclass
class Keyword(Base):
    id: int
    keyword: str
