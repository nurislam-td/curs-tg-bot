from aiogram.types import Message

from aiogram.filters import BaseFilter
from app.adapters.tokenizer import NLTKTokenizer
from app.adapters.unit_of_work import SQLAlchemyUnitOfWork


class HasKeyword(BaseFilter):
    def __init__(self):
        self.tokenizer = NLTKTokenizer()
        self.uow = SQLAlchemyUnitOfWork()

    async def __call__(self, message: Message):
        text_words = self.tokenizer.process_text(message.text)
        text_words_set = set(text_words)
        async with self.uow:
            keywords = await self.uow.keyword.get_by_keywords(text_words_set)
        if keywords:
            return {"keywords": keywords, "uow": self.uow}
        return False
