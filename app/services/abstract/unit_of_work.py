from abc import ABC, abstractmethod
from app.services.abstract.repo import KeywordGroupRepo


class UnitOfWork(ABC):
    keyword_group: KeywordGroupRepo

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
