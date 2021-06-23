from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from structlog import get_logger

from settings import settings


engine = create_engine(settings.get_uri(), echo=True)
base = declarative_base()


class SqlAlchemy:

    session = None

    def __init__(self, engine, base):
        self.engine = engine
        self.base = base
        self.logger = get_logger()

    def init_connection(self):
        from apps import models_hub
        self.base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()
        self.logger.debug('Database connection initialized')


db = SqlAlchemy(engine=engine, base=base)
