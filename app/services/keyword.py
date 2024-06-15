from app.services.abstract.unit_of_work import UnitOfWork
from app.services.abstract.tokenizer import Tokenizer
from app.services.entity.keyword import (
    KeywordGroupCreate,
    KeywordGroupMapCreate,
    KeywordGroupDTO,
    KeywordCreate,
)


async def set_keywords(
    keywords_text: str, group: KeywordGroupDTO, uow: UnitOfWork, tokenizer: Tokenizer
):
    tokens = tokenizer.process_text(keywords_text)
    tokens = set(tokens)
    keywords = [KeywordCreate(keyword=token).model_dump() for token in tokens]
    async with uow:
        await uow.keyword.create_if_not_exists(keywords)
        keyword_group_map = [
            KeywordGroupMapCreate(keyword_id=keyword["id"], group_id=group.id)
            for keyword in keywords
        ]
        await uow.keyword_group_map.create_keywords_group_maps(keyword_group_map)
        await uow.commit()
    return keywords  # TODO


async def get_keyword_groups(uow: UnitOfWork) -> list[KeywordGroupDTO]:
    async with uow:
        keyword_groups = await uow.keyword_group.get_all()
    return keyword_groups


async def get_keyword_group(uow: UnitOfWork, group_title: str) -> KeywordGroupDTO:
    async with uow:
        keyword_group = await uow.keyword_group.get_by_title(group_title)
    return keyword_group


async def add_group(uow: UnitOfWork, group: KeywordGroupCreate) -> KeywordGroupDTO:
    async with uow:
        keyword_group = await uow.keyword_group.create(values=group.model_dump())
        await uow.commit()
    return keyword_group
