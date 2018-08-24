from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import desc
from models import Samples
import os

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "root"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "root"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "localhost"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "samples"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()
    
    def _get_session(self):
        """Singleton of db connection

        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session
    def get_last_sample(self):
        session=self._get_session()
        query = session.query(Samples).order_by(desc(Samples.id))
        sample = query.first()
        session.close()
        return sample
    def insert_sample(self, sample):
        session=self._get_session()
        session.add(sample)
        session.commit()
        session.close()
    def get_average_sample(self):
        temp=0
        humedad=0
        presion=0
        viento=0
        session=self._get_session()
        query = session.query(Samples).order_by(desc(Samples.id)).limit(10)
        samples = query.all()
        for s in samples:
            temp=temp+s.temperature
            humedad=humedad+s.humidity
            presion=presion+s.pressure
            viento=viento+s.windspeed
        average=Samples()
        average.temperature=float(temp)/10
        average.humidity=float(humedad)/10
        average.pressure=float(presion)/10
        average.windspeed=float(viento)/10
        session.close()
        return average