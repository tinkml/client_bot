from enum import Enum
from typing import List

from aiogram import types


class EnumCommands(Enum):

    @classmethod
    def get_bot_commands_list(cls) -> List[types.BotCommand]:
        return [types.BotCommand(x.name, x.value) for x in cls]

    @classmethod
    def get_keyboard_buttons_list(cls) -> List[types.KeyboardButton]:
        return [types.KeyboardButton(text=x.value) for x in cls]

    @property
    def keyboard_button(self):
        return types.KeyboardButton(text=self.value)
