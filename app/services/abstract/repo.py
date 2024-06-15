from abc import abstractmethod, ABC
from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import Select

from app.services.entity.chat import ChatDTO, ChatCreate
from app.services.entity.keyword import (
    KeywordGroupDTO,
    KeywordDTO,
    KeywordGroupMapDTO,
    KeywordGroupMapCreate,
    KeywordCreate,
    KeywordMapDTO,
    KeywordMapCreate,
)
from app.services.entity.reports import ReportDTO
from app.services.entity.user import TGUserDTO, TGUserCreate

DTO = TypeVar("DTO", bound=BaseModel)


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


class KeywordGroupRepo(Repo[KeywordGroupDTO], ABC):
    @abstractmethod
    async def get_by_title(self, title: str) -> KeywordGroupDTO | None: ...


class KeywordRepo(Repo[KeywordDTO], ABC):
    @abstractmethod
    async def create_if_not_exists(
        self,
        keywords: list[KeywordCreate],
    ) -> None: ...

    @abstractmethod
    async def get_by_keywords(self, keywords: set[str]) -> list[KeywordDTO] | None: ...


class KeywordGroupMapRepo(Repo[KeywordGroupMapDTO], ABC):
    @abstractmethod
    async def create_keywords_group_maps(
        self, keyword_group_maps: list[KeywordGroupMapCreate]
    ) -> None: ...


class KeywordMapRepo(Repo[KeywordMapDTO], ABC):
    @abstractmethod
    async def create_many(self, keyword_maps: list[KeywordMapCreate]) -> None: ...

    @abstractmethod
    async def get_by_week(self, *args, **kwargs) -> list[KeywordMapDTO]: ...


class TGUserRepo(Repo[TGUserDTO], ABC):
    @abstractmethod
    async def create_if_not_exists(self, tg_user: TGUserCreate) -> None: ...


class ChatRepo(Repo[ChatDTO], ABC):
    @abstractmethod
    async def create_if_not_exists(self, chat: ChatCreate) -> None: ...


class ReportRepo(Repo[ReportDTO], ABC):
    @abstractmethod
    def get_by_week(self) -> Select: ...

    @abstractmethod
    async def create_for_week(self) -> None: ...
