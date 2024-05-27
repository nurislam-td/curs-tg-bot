from abc import abstractmethod, ABC
from typing import Generic, TypeVar
from uuid import UUID

from app.services.keyword import KeywordGroup

DTO = TypeVar("DTO")


class Repo(Generic[DTO]):
    @abstractmethod
    async def create(self, values: dict) -> DTO | None: ...

    @abstractmethod
    async def get_all(self, **kwargs) -> list[DTO] | None: ...

    @abstractmethod
    async def get(self, pk: UUID | int) -> DTO | None: ...

    @abstractmethod
    async def update(self, values: dict, filters: dict) -> list[DTO] | None: ...

    @abstractmethod
    async def update_one(self, values: dict, pk: UUID | int) -> DTO | None: ...

    @abstractmethod
    async def delete(self, filters: dict) -> None: ...


class KeywordGroupRepo(Repo[KeywordGroup], ABC):
    pass
