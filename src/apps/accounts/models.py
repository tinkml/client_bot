from sqlalchemy import Column, String, Integer

from db.init_db import base


class Account(base):

    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, session, name, age, gender):
        self.session = session
        self.name = name
        self.age = age
        self.gender = gender

    def create(self):
        self.session.add(self)
        self.session.commit()


