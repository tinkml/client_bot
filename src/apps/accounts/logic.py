from typing import Tuple, Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from apps.accounts import schemas, service
from apps.accounts.texts import SignUpTexts
from apps.commands import KeyBoard, SelectionCommands, StateCommands


async def cancel_states_and_keyboards(state: FSMContext) -> Tuple[str, types.ReplyKeyboardRemove]:
    """Обнуляет машину состояний, если было состояние, удаляет клавиатуру."""
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    return SignUpTexts.canceled.value, types.ReplyKeyboardRemove()


def start_sign_up(message: types.Message) -> Tuple[str, types.ReplyKeyboardMarkup]:
    """Отдает текст и клавиатуру для запуска сценария регистрации."""
    chat_data = message.chat.values
    text = SignUpTexts.start_sign_up.value.format(first_name=chat_data['first_name'], last_name=chat_data['last_name'])

    keyboard = KeyBoard.get_keyboard(([SignUpTexts.fullname_confirmation.value],))
    keyboard.add(StateCommands.cancel.keyboard_button)
    return text, keyboard


async def process_fullname_for_sign_up(
        message: types.Message,
        state: FSMContext
) -> Tuple[str, types.ReplyKeyboardMarkup]:
    """
    Сохраняет данные чата в машине состояний.
    Отдает текст и клавиатуру для продолжения сценария регистрации.
    """
    chat_data = message.chat.values
    if message.text != SignUpTexts.fullname_confirmation.value:
        chat_data['first_name'], chat_data['last_name'] = message.text.split(' ')
    await state.update_data(chat_data=chat_data)

    text = SignUpTexts.is_user_a_legal_entity.value
    keyboard = KeyBoard.get_keyboard((SelectionCommands.get_keyboard_buttons_list(), ))
    keyboard.add(StateCommands.cancel.keyboard_button)
    return text, keyboard


async def process_is_legal_entity_for_sign_up(
        message: types.Message,
        state: FSMContext
) -> Tuple[str, Union[types.ReplyKeyboardMarkup, types.ReplyKeyboardRemove]]:
    """
    Сохраняет данные является ли пользователь Юр. лицом, в машину состояний.
    Отдает текст и клавиатуру для завершения сценария регистрации.
    Валидирует полученный ответ.
    """
    if message.text.lower() not in [x.value for x in SelectionCommands]:
        text = SignUpTexts.is_legal_entity_incorrect_answer.value
        keyboard = KeyBoard.get_keyboard((SelectionCommands.get_keyboard_buttons_list(), ))
        keyboard.add(StateCommands.cancel.keyboard_button)

    else:
        await state.update_data(is_legal_entity=SelectionCommands(message.text.lower()).bool_value)
        data = await state.get_data()
        schema = schemas.AccountCreate(**data['chat_data'], is_legal_entity=data['is_legal_entity'])
        await service.AccountService.create(data=schema.dict())
        await state.finish()
        text = SignUpTexts.sign_up_is_over.value
        keyboard = types.ReplyKeyboardRemove()

    return text, keyboard
