from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey

from src.db.base import base


class Account(base):

    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    first_name = Column(String(length=255))
    last_name = Column(String(length=255), nullable=True)
    username = Column(String(length=255), nullable=True)
    email = Column(String(length=128), nullable=True, unique=True)
    phone = Column(String(length=64), unique=True)
    is_legal_entity = Column(Boolean, default=False)
    registration_at = Column(DateTime, default=datetime.utcnow())


class LegalEntityData(base):
    """
    Данные Юр. лица.
    Используется если пользователь регистрируется в качестве Юр.лица
    """
    __tablename__ = 'legal_entity_data'

    id = Column(Integer, primary_key=True)
    account = Column(ForeignKey('account.id', ondelete='CASCADE'), nullable=False)
    inn = Column(String(length=12), nullable=True, unique=True)
    company_kpp = Column(String(length=64), nullable=True)
    company_ogrn = Column(String(length=64), nullable=True)
    company_name = Column(String(length=128), nullable=True)
    company_address = Column(String(length=255), nullable=True)


class BankData(base):
    """
    Данные о банковских реквизиты.
    Используется если пользователь регистрируется в качестве Юр.лица
    """
    __tablename__ = 'bank_data'

    id = Column(Integer, primary_key=True)
    legal_entity_data = Column(ForeignKey('legal_entity_data.id', ondelete='CASCADE'), nullable=False)
    bank_name = Column(String(length=128), nullable=True)
    bank_bik = Column(String(length=32), nullable=True)
    correspondent_account = Column(String(length=32), nullable=True)
    personal_account = Column(String(length=32), nullable=True)
