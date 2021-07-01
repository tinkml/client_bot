from aiogram import types
from aiogram.dispatcher import FSMContext

from apps.commands import StateCommands
from initializer import dp, bot
from . import logic
from .enums import AccountCommands as cmd
from .states import SignUpForm


@dp.message_handler(commands=StateCommands.cancel.name, state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """Обрабатывает команду отмены."""
    text, keyboard = await logic.cancel_states_and_keyboards(state=state)
    await message.reply(text, reply_markup=keyboard)


@dp.message_handler(commands=cmd.sign_up.name)
async def handle_sign_up(message: types.Message):
    """Запускает сценарий регистрации пользователя."""
    await SignUpForm.chat_data.set()
    text, keyboard = logic.start_sign_up(message=message)
    await message.reply(text, reply_markup=keyboard)


@dp.message_handler(state=SignUpForm.chat_data)
async def handle_fullname_for_sign_up(message: types.Message, state: FSMContext):
    """Обрабатывает 1-й шаг сценария регистрации - получение данных чата."""
    text, keyboard = await logic.process_fullname_for_sign_up(message=message, state=state)
    await SignUpForm.next()
    await message.reply(text, reply_markup=keyboard)


@dp.message_handler(state=SignUpForm.is_legal_entity)
async def handle_is_legal_entity_for_sign_up(message: types.Message, state: FSMContext):
    """Обрабатывает 2-й шаг сценария регистрации - является ли пользователь Юр. лицом."""
    text, keyboard = await logic.process_is_legal_entity_for_sign_up(message=message, state=state)
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)
