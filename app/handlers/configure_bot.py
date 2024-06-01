from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.keyboards.text import CallbackDataText
from app.states.configure_bot import ConfigureBot

router = Router()


@router.callback_query(F.data == CallbackDataText.configure_bot)
async def configure_bot_start(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await state.set_state(ConfigureBot.keywords)
    await callback_query.message.answer(
        text="Напишите мне ключевые слова которые вы бы хотели отслеживать"
    )


@router.message()
async def configure_bot_set_keywords(message: Message):
    pass
