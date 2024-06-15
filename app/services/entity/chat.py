from pydantic import BaseModel


class ChatCreate(BaseModel):
    id: int
    title: str | None = None
    description: str | None = None


class ChatDTO(BaseModel):
    id: int
    title: str | None = None
    description: str = None
