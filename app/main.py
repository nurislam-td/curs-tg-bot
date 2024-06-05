import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.config.settings import settings
from app.handlers import bot_router


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    dp.include_router(bot_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start())
