from abc import abstractmethod, ABC
from typing import Generic, TypeVar

from app.services.entity.keyword import KeywordGroup, Keyword

DTO = TypeVar("DTO")


class Repo(Generic[DTO]):
    @abstractmethod
    async def create(self, values: dict) -> DTO | None: ...

    @abstractmethod
    async def get_all(self, **kwargs) -> list[DTO] | None: ...

    @abstractmethod
    async def get(self, pk: str | int) -> DTO | None: ...

    @abstractmethod
    async def update(self, values: dict, filters: dict) -> list[DTO] | None: ...

    @abstractmethod
    async def update_one(self, values: dict, pk: str | int) -> DTO | None: ...

    @abstractmethod
    async def delete(self, filters: dict) -> None: ...


class KeywordGroupRepo(Repo[KeywordGroup], ABC):
    pass


class KeywordRepo(Repo[Keyword], ABC):
    @abstractmethod
    async def create_if_not_exists(
        self, keywords: list[str]
    ) -> list[Keyword] | None: ...
