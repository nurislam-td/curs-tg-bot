from app.services.abstract.unit_of_work import UnitOfWork
from app.services.abstract.tokenizer import Tokenizer
from app.services.entity.chat import ChatCreate
from app.services.entity.keyword import (
    KeywordGroupCreate,
    KeywordGroupMapCreate,
    KeywordGroupDTO,
    KeywordCreate,
    KeywordDTO,
    KeywordMapCreate,
)
from app.services.entity.user import TGUserCreate


async def set_keywords(
    keywords_text: str, group: KeywordGroupDTO, uow: UnitOfWork, tokenizer: Tokenizer
):
    tokens = tokenizer.process_text(keywords_text)
    tokens = set(tokens)
    keywords = [KeywordCreate(keyword=token) for token in tokens]
    async with uow:
        await uow.keyword.create_if_not_exists(keywords)
        keywords_db: list[KeywordDTO] = await uow.keyword.get_by_keywords(
            keywords=tokens
        )

        keyword_group_map = [
            KeywordGroupMapCreate(keyword_id=keyword.id, group_id=group.id)
            for keyword in keywords_db
        ]
        await uow.keyword_group_map.create_keywords_group_maps(keyword_group_map)
        await uow.commit()
    return keywords_db


async def get_keyword_groups(uow: UnitOfWork) -> list[KeywordGroupDTO]:
    async with uow:
        keyword_groups = await uow.keyword_group.get_all()
    return keyword_groups


async def get_keyword_group(uow: UnitOfWork, group_id: int) -> KeywordGroupDTO:
    async with uow:
        keyword_group = await uow.keyword_group.get(group_id)
    return keyword_group


async def add_group(uow: UnitOfWork, group: KeywordGroupCreate) -> KeywordGroupDTO:
    async with uow:
        keyword_group = await uow.keyword_group.create(values=group.model_dump())
        await uow.commit()
    return keyword_group


async def save_keyword_map(
    tg_user: TGUserCreate, chat: ChatCreate, keywords: list[KeywordDTO], uow: UnitOfWork
):
    async with uow:
        await uow.tg_user.create_if_not_exists(tg_user)
        await uow.chat.create_if_not_exists(chat)
        keyword_maps = [
            KeywordMapCreate(
                keyword_id=keyword.id, chat_id=chat.id, tg_user_id=tg_user.id
            )
            for keyword in keywords
        ]
        await uow.keyword_map.create_many(keyword_maps)
        await uow.commit()
