import os

from src.db.settings import DataBaseSettings


class Settings(DataBaseSettings):

    BOT_TOKEN: str = None

    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 7001

    DOMAIN: str = ''
    WEBHOOK_PATH: str = '/api/v1'
    WEBHOOK_URL = DOMAIN + WEBHOOK_PATH

    class Config:
        # for local development without docker
        # broken source .env
        env_file = os.getenv('ENV_FILE')


settings = Settings()
