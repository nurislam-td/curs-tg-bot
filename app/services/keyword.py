from app.services.abstract.unit_of_work import UnitOfWork
from app.services.abstract.tokenizer import Tokenizer
from app.services.entity.keyword import KeywordGroup


async def set_keywords(keywords_text: str, uow: UnitOfWork, tokenizer: Tokenizer):
    keywords = "".join(keywords_text.split(" ")).split(",")
    tokens = [tokenizer.tokenize_word(keyword) for keyword in keywords]
    async with uow:
        created = await uow.keyword.create_if_not_exists(tokens)
        await uow.commit()
    return created


async def create_keyword_group(
    keyword_group: KeywordGroup, uow: UnitOfWork
) -> KeywordGroup:
    async with uow:
        created = await uow.keyword_group.create(values=keyword_group.as_dict())
        await uow.commit()
    return created


async def get_keyword_groups(uow: UnitOfWork) -> list[KeywordGroup]:
    async with uow:
        keyword_groups = await uow.keyword_group.get_all()
    return keyword_groups
