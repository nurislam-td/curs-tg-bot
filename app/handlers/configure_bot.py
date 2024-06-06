from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from app.keyboards.text import CallbackDataText
from app.keyboards.inline import get_group_select_keyboard
from app import dependencies
from app.services.abstract.unit_of_work import UnitOfWork
from app.services.abstract.tokenizer import Tokenizer
from app.services.entity.keyword import KeywordGroup
from app.states.configure_bot import ConfigureBot
from app.services import keyword

router = Router()


@router.callback_query(
    F.data == CallbackDataText.configure_bot, dependencies.UnitOfWork()
)
async def configure_bot_start(callback_query: CallbackQuery, uow: UnitOfWork):
    await callback_query.answer()
    groups = await keyword.get_keyword_groups(uow)
    await callback_query.message.answer(
        text="Выберите группу в которую вы хотите добавить слова или создайте новую",
        reply_markup=await get_group_select_keyboard(groups=groups),
    )


@router.callback_query(
    F.data == CallbackDataText.select_group, dependencies.UnitOfWork()
)
async def configure_bot_select_groups(
    callback_query: CallbackQuery, state: FSMContext, uow
):
    selected_group = callback_query.message.text
    group = keyword.get_keyword_group(uow=uow, group_title=selected_group)
    await state.update_data(group=group)
    await state.set_state(ConfigureBot.keywords)
    await callback_query.message.answer(
        text=f"Наберите слова которые вы хотите добавить в группу {selected_group} через запятую"
    )


@router.callback_query(F.data == CallbackDataText.add_group, dependencies.UnitOfWork())
async def configure_bot_add_group(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await state.set_state(ConfigureBot.group_title)
    await callback_query.message.answer(
        text="Введите заголовок группы", reply_markup=ReplyKeyboardRemove()
    )


@router.message(ConfigureBot.group_title, dependencies.UnitOfWork())
async def configure_bot_add_group_title(message: Message, state: FSMContext):
    await state.set_state(ConfigureBot.group_description)
    await state.update_data(group_title=message.text)
    await message.answer(text="Введите описание для группы")


@router.message(ConfigureBot.group_description, dependencies.UnitOfWork())
async def configure_bot_add_group_description(
    message: Message, state: FSMContext, uow: UnitOfWork
):
    group_info = await state.get_data()
    group = KeywordGroup(
        title=group_info["group_title"],
        description=message.text,
    )
    await state.clear()
    group = await keyword.add_group(uow=uow, group=group)
    await state.update_data(group=group)

    await message.answer(
        text="Супер группа была добавлена, наберите слова которые вы хотите добавить в группу"
    )
    await state.set_state(ConfigureBot.keywords)


@router.message(
    ConfigureBot.keywords, dependencies.UnitOfWork(), dependencies.Tokenizer()
)
async def configure_bot_set_keywords(
    message: Message, state: FSMContext, uow: UnitOfWork, tokenizer: Tokenizer
):
    keywords_text = message.text
    data = await state.get_data()
    await state.clear()
    await keyword.set_keywords(
        keywords_text=keywords_text, group=data["group"], uow=uow, tokenizer=tokenizer
    )
    await message.answer(
        text="Супер, слова добавлены в группу",
    )
