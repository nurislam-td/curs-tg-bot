__all__ = ("bot_router",)

from .configure_bot import router as configure_bot_router
from .command import router as command_router
from .reports import router as report_router
from .user_message import router as user_message_router
from aiogram import Router

bot_router = Router()
bot_router.include_routers(
    configure_bot_router, command_router, report_router, user_message_router
)
