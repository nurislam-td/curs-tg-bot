from aiogram.fsm.state import State, StatesGroup


class ConfigureBot(StatesGroup):
    keywords = State()
    group_title = State()
    group_description = State()
