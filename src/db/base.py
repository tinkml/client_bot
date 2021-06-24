from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from structlog import get_logger

from src.settings import settings

engine = create_async_engine(settings.get_db_uri(), echo=True)
base = declarative_base()


class SqlAlchemy:

    async_session = None

    def __init__(self, engine, base):
        self.engine = engine
        self.base = base
        self.logger = get_logger()

    async def init_connection(self):
        self.async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
        self.logger.debug('Database connection initialized')


db = SqlAlchemy(engine=engine, base=base)
