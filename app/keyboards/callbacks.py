from aiogram.filters.callback_data import CallbackData


class KeywordGroupCallback(CallbackData, prefix="keyword_group"):
    action: str
    group_id: int
    title: str
