from abc import ABC, abstractmethod
from app.services.abstract.repo import (
    KeywordGroupRepo,
    KeywordRepo,
    KeywordGroupMapRepo,
    KeywordMapRepo,
    TGUserRepo,
    ChatRepo,
    ReportRepo,
)


class UnitOfWork(ABC):
    keyword_group: KeywordGroupRepo
    keyword: KeywordRepo
    keyword_map: KeywordMapRepo
    keyword_group_map: KeywordGroupMapRepo
    tg_user: TGUserRepo
    chat: ChatRepo
    report: ReportRepo

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __call__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...
