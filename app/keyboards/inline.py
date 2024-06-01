from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.keyboards.text import CallbackDataText, ButtonText


def get_config_button():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=ButtonText.configure_bot, callback_data=CallbackDataText.configure_bot
    )
