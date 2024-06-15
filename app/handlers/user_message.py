from aiogram import Router
from aiogram.types import Message

from app.filters.has_keyword import HasKeyword
from app.services.abstract.unit_of_work import UnitOfWork
from app.services.entity.chat import ChatCreate
from app.services.entity.keyword import KeywordDTO
from app.services.entity.user import TGUserCreate
from app.services import keyword

router = Router(name=__name__)


@router.message(HasKeyword())
async def save_keyword_map(
    message: Message, keywords: list[KeywordDTO], uow: UnitOfWork
):
    user = message.from_user
    chat = message.chat
    tg_user = TGUserCreate(id=user.id, username=user.username)
    chat_model = ChatCreate(id=chat.id, title=chat.title, description=chat.description)
    await keyword.save_keyword_map(
        tg_user=tg_user, chat=chat_model, keywords=keywords, uow=uow
    )
