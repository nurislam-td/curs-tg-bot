from aiogram.types import Message

from app.services.abstract.unit_of_work import UnitOfWork
from app.adapters.unit_of_work import SQLAlchemyUnitOfWork
from app.adapters.tokenizer import NLTKTokenizer
from aiogram.filters import BaseFilter


def get_uow() -> UnitOfWork:
    return SQLAlchemyUnitOfWork()


class UnitOfWork(BaseFilter):
    def __init__(self):
        self.uow = SQLAlchemyUnitOfWork()

    async def __call__(self, message: Message):
        return {"uow": self.uow}


class Tokenizer(BaseFilter):
    def __init__(self):
        self.tokenizer = NLTKTokenizer()

    async def __call__(self, message: Message):
        return {"tokenizer": self.tokenizer}
