from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.keyboards.text import CallbackDataText
from app.states.configure_bot import ConfigureBot
from app.services import keyword

router = Router()


@router.callback_query(F.data == CallbackDataText.configure_bot)
async def configure_bot_start(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await state.set_state(ConfigureBot.keywords)
    await callback_query.message.answer(
        text="Напишите мне ключевые слова которые вы бы хотели отслеживать"
    )


@router.message(ConfigureBot.keywords)
async def configure_bot_set_keywords(message: Message, state: FSMContext):
    keywords_text = message.text
    await keyword.set_keywords(keywords_text, uow, tokenizer)
    await state.set_state(ConfigureBot.group_title)
    await message.answer(
        text="Супер, выберите группу в которую вы хотите добавить слова или создайте новую",
        reply_markup=get_group_select_keyboard(),
    )
    # TODO done this
