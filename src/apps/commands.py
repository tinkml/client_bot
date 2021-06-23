from aiogram import types

from accounts.enums import AccountCommands


class Commands(AccountCommands):

    start = 'Запустить бота'
    help = 'Вывести справку'


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(x.name, x.value) for x in Commands

        ]
    )