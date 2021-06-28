from pydantic import BaseSettings


class DataBaseSettings(BaseSettings):

    POSTGRES_USER: str = 'helper'
    POSTGRES_PASSWORD: str = 'helper'
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_DB: str = 'helper'

    MIGRATIONS_DIR = 'migrations'

    def get_db_uri(self):
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:5432/{self.POSTGRES_DB}'
