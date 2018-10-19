#!/usr/bin/python
#
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy import update
from sqlalchemy import desc

class Database(object):
    Base = declarative_base()
    session = None

    def __get_session(self):
        if self.session == None:
            url_sqlite = 'sqlite:///database/panel-control.db'
            engine = create_engine(url_sqlite,convert_unicode=True,echo=True)
            Session = scoped_session(sessionmaker(autocommit=False,autoflush=True,bind=engine))
            self.session = Session()
            self.Base.metadata.create_all(engine)            
        return self.session

    def insert_user(self, User):
        session=self.__get_session()
        session.add(User)
        session.commit()
        session.close()

    def update_password(self,User):
        session = self.__get_session()
        user = session.query(models.User).filter(models.User.username == User.username).first()
        user.password = User.password
        session.commit()
        session.close()

    def insert_pin(self, Pin):
        session=self.__get_session()
        session.add(Pin)
        session.commit()
        session.close()

    def update_pin(self, Pin):
        session=self.__get_session()
        pin = session.query(models.Pin).filter(models.Pin.pin == Pin.pin).first()
        pin.state = Pin.state
        pin.ty = Pin.ty
        session.commit()
        session.close()

    def delete_pin(self, Pin):
        session=self.__get_session()
        query =  session.query(Pin).filter(pin=Pin.pin).delete(synchronize_session=False)
        session.commit()
        session.close()
        
    def get_user(self, User):
        session = self.__get_session()
        user = session.query(models.User).filter(models.User.username == User.username).first()
        session.close()
        return user
    
    def get_pin(self, Pin):
        session = self.__get_session()
        pin = session.query(models.Pin).filter(models.Pin.pin == Pin.pin).first()
        session.close()
        return pin

    def get_all_pin(self):
        session = self.__get_session()
        pins = session.query(models.Pin).all()
        return pins 

