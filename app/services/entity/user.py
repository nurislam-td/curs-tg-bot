from pydantic import BaseModel


class TGUserCreate(BaseModel):
    id: int
    username: str


class TGUserDTO(BaseModel):
    id: int
    username: str
