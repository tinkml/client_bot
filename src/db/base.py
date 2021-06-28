import configparser
import os
from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from structlog import get_logger

from src.settings import settings

engine = create_async_engine(settings.get_db_uri(), echo=True)
base = declarative_base()


class AlembicMigrator:

    alembic_ini_path = os.path.join(settings.BASE_PATH, 'alembic.ini')
    migration_dir_path = os.path.join(settings.BASE_PATH, settings.MIGRATIONS_DIR)

    @classmethod
    def _init_alembic(cls):
        """
        Инициализирует alembic.
        Создает директорию для миграций, конфигурирует файл env.py,
        подключая объект metadata для автоматических миграций.
        """
        if not os.path.exists(cls.migration_dir_path):
            os.system(f"alembic init --template async {settings.MIGRATIONS_DIR}")

            migration_env_script = os.path.join(cls.migration_dir_path, 'env.py')
            with open(migration_env_script, 'r+') as env_file:
                file_data = env_file.read()
                file_data = file_data.replace(
                    'target_metadata = None',
                    'from src.apps import models_hub\ntarget_metadata = models_hub.base.metadata'
                )
                env_file.seek(0)
                env_file.truncate()
                env_file.write(file_data)

    @classmethod
    def _config_alembic_ini(cls):
        """Конфигурирует файл alembic.ini """
        config = configparser.ConfigParser()
        config.read(cls.alembic_ini_path)

        config.set('alembic', 'script_location', cls.migration_dir_path)
        config.set('alembic', 'sqlalchemy.url', settings.get_db_uri())

        with open(cls.alembic_ini_path, 'w') as config_file:
            config.write(config_file)

    @classmethod
    def make_migrations(cls):
        """Создает и устанавливает миграции."""
        cls._init_alembic()
        cls._config_alembic_ini()
        os.system(f"alembic -c {cls.alembic_ini_path} revision --autogenerate -m '{date.today()}'")
        os.system(f"alembic -c {cls.alembic_ini_path} upgrade head")


class SqlAlchemy:

    async_session = None

    def __init__(self, engine, base):
        self.engine = engine
        self.base = base
        self.logger = get_logger()

    async def init_connection(self):
        AlembicMigrator.make_migrations()
        self.async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
        self.logger.debug('Database connection initialized')


db = SqlAlchemy(engine=engine, base=base)
