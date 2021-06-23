from utils.misc import EnumCommands
from .accounts.enums import AccountCommands


class ServiceCommands(EnumCommands):

    start = 'Запустить бота'
    help = 'Вывести справку'


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            *AccountCommands.get_commands_list(),
            *ServiceCommands.get_commands_list(),
        ]
    )
