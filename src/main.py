from aiogram.utils.executor import start_webhook

from apps import handlers_hub

from apps.commands import set_default_commands
from db.base import db
from initializer import dp, bot
from settings import settings


async def on_startup(dispatcher):
    await bot.set_webhook(url=settings.WEBHOOK_URL)
    await set_default_commands(dispatcher)
    await db.init_connection()


async def on_shutdown(dispatcher):
    ...


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=settings.WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT
    )
