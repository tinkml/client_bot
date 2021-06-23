from enum import Enum
from typing import List

from aiogram import types


class EnumCommands(Enum):

    @classmethod
    def get_commands_list(cls) -> List[types.BotCommand]:
        return [types.BotCommand(x.name, x.value) for x in cls]
