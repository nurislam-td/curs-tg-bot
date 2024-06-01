from aiogram import Router
from aiogram.types import Message
from app.keyboards.inline import get_config_button

router = Router()


@router.message(command="start")
async def start_command(message: Message):
    await message.answer(
        "Для начала работы бота его нужно настроить, нажмите кнопку ниже",
        reply_markup=get_config_button(),
    )
