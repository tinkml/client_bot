from sqlalchemy import Column, String, Integer

from db.base import base


class Account(base):

    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
