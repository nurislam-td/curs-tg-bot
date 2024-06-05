from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.keyboards.text import CallbackDataText, ButtonText
from app.services.entity.keyword import KeywordGroup


def get_config_button():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=ButtonText.configure_bot, callback_data=CallbackDataText.configure_bot
    )
    return builder.as_markup()


async def get_group_select_keyboard(groups: list[KeywordGroup] | None):
    builder = InlineKeyboardBuilder()
    if groups:
        for group in groups:
            builder.button(
                text=group.title, callback_data=CallbackDataText.select_group
            )
    builder.button(text="Добавить группу", callback_data=CallbackDataText.add_group)
    return builder.as_markup()
