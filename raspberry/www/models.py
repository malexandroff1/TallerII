from sqlalchemy import Column, Integer, String
import database
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(150), unique=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username

class Pin(Base):
    __tablename__ = 'pins'
    id = Column(Integer, primary_key=True)
    pin = Column(Integer, unique=True)
    state = Column(String(10), unique=True)

    def __init__(self, pin=None, state=None):
        self.pin = pin
        self.state = state

    def __repr__(self):
        return self.state

