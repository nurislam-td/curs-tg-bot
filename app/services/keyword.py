from app.services.abstract.unit_of_work import UnitOfWork
from app.services.abstract.tokenizer import Tokenizer
from app.services.entity.keyword import KeywordGroup, KeywordGroupMap


async def set_keywords(
    keywords_text: str, group: KeywordGroup, uow: UnitOfWork, tokenizer: Tokenizer
):
    keywords = "".join(keywords_text.split(" ")).split(",")
    tokens = [tokenizer.tokenize_text(keyword) for keyword in keywords]
    async with uow:
        created = await uow.keyword.create_if_not_exists(tokens)
        keyword_group_map = [
            KeywordGroupMap(keyword_id=keyword.id, group_id=group.id)
            for keyword in created
        ]
        await uow.keyword_group_map.create_keywords_group_maps(keyword_group_map)
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


async def get_keyword_group(uow: UnitOfWork, group_title: str) -> KeywordGroup:
    async with uow:
        keyword_group = await uow.keyword_group.get_by_title(group_title)
    return keyword_group


async def add_group(uow: UnitOfWork, group: KeywordGroup) -> KeywordGroup:
    async with uow:
        keyword_group = await uow.keyword_group.create(values=group.as_dict())
    return keyword_group
