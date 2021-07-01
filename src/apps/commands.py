from typing import List, Tuple, Union

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.misc import EnumCommands
from .accounts.enums import AccountCommands


class ServiceCommands(EnumCommands):

    start = 'запустить бота'
    help = 'вывести справку'


class StateCommands(EnumCommands):

    cancel = 'отмена'
    skip = 'пропустить'


class SelectionCommands(EnumCommands):

    yes = 'да'
    no = 'нет'

    @property
    def bool_value(self):
        if self == self.yes:
            return True
        elif self == self.no:
            return False


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            *AccountCommands.get_bot_commands_list(),
            *ServiceCommands.get_bot_commands_list(),
        ]
    )


class KeyBoard:

    @classmethod
    def get_keyboard(
            cls, commands_name_or_button: Tuple[List[str or KeyboardButton]]
    ) -> ReplyKeyboardMarkup:
        """"""
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=True)
        for name_or_button in commands_name_or_button:
            keyboard.add(*name_or_button)

        return keyboard
