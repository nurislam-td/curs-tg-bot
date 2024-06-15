import uuid

from pydantic import BaseModel, Field


class KeywordGroupCreate(BaseModel):
    title: str
    description: str
    is_active: bool = True


class KeywordCreate(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    keyword: str


class KeywordGroupMapCreate(BaseModel):
    keyword_id: int
    group_id: int


class KeywordGroupDTO(BaseModel):
    id: int
    title: str
    description: str
    is_active: bool = True


class KeywordDTO(BaseModel):
    id: int
    keyword: str


class KeywordGroupMapDTO(BaseModel):
    id: int
    keyword_id: int
    group_id: int
