from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database(object):
    Base = declarative_base()

    def __get_session(self):
        if self.session == None:
            connection = '../database/panel-control.db'
            engine = create_engine(connection,convert_unicode=True,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session

    def insert_user(self, User):
        session=self.__get_session()
        session.add(User)
        session.commit()
        session.close()

    def update_password(self,User):
        session=self.__get_session()
        query =  session.query.filter_by(username=User.username).update(dict(password= User.password))
        session.commit()
        session.close()

    def insert_pin(self, Pin):
        session=self.__get_session()
        session.add(Pin)
        session.commit()
        session.close()

    def update_pin(self, Pin):
        session=self.__get_session()
        query =  session.query.filter_by(pin=Pin.pin).update(dict(state= Pin.state))
        session.commit()
        session.close()

    def delete_pin(self, Pin):
        session=self.__get_session()
        query =  session.query(Pin).filter(pin=Pin.pin).delete(synchronize_session=False)
        session.commit()
        session.close()