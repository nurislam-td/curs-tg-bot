from pydantic import BaseModel


class KeywordGroupCreate(BaseModel):
    title: str
    description: str
    is_active: bool = True


class KeywordCreate(BaseModel):
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
