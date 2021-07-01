from aiogram.dispatcher.filters.state import State, StatesGroup


class SignUpForm(StatesGroup):
    chat_data = State()
    is_legal_entity = State()
