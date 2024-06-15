from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.keyboards.text import CallbackDataText, ButtonText
from app.services.entity.keyword import KeywordGroupDTO
from app.keyboards.callbacks import KeywordGroupCallback


def get_config_button():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=ButtonText.configure_bot, callback_data=CallbackDataText.configure_bot
    )
    return builder.as_markup()


async def get_group_select_keyboard(groups: list[KeywordGroupDTO] | None):
    builder = InlineKeyboardBuilder()
    if groups:
        for group in groups:
            builder.button(
                text=group.title,
                callback_data=KeywordGroupCallback(
                    action=CallbackDataText.select_group,
                    group_id=group.id,
                    title=group.title,
                ),
            )

    builder.button(text="Добавить группу", callback_data=CallbackDataText.add_group)
    builder.adjust(1)

    return builder.as_markup()
