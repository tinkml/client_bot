import os
from enum import Enum

from pydantic import BaseSettings

from src.db.settings import DataBaseSettings


class ServerSettings(BaseSettings):

    BOT_TOKEN: str = None
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 7001

    DOMAIN: str = ''
    WEBHOOK_PATH: str = '/api/v1'

    class EnvMode(Enum):
        dev = 'DEV'
        prod = 'PROD'

    ENV: EnvMode = EnvMode.prod

    def get_webhook_url(self):
        return self.DOMAIN + self.WEBHOOK_PATH


class Settings(DataBaseSettings, ServerSettings):

    BASE_PATH = '/app'

    class Config:
        # for local development without docker
        # broken source .env
        env_file = os.getenv('ENV_FILE')


settings = Settings()
