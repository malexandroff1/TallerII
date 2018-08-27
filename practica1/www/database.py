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
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
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
    #funcion que retorna la ultima medida almacenada en la base de datos
    #retorna un objeto sample
    def get_last_sample(self):
        #obtiene la sesion
        session=self._get_session()
        #obtiene las medidas ordenadas por id en forma descendente
        query = session.query(Samples).order_by(desc(Samples.id))
        #obtiene la ultima medida
        sample = query.first()
        session.close()
        return sample
    #funcion que inserta las mediciones a la base de datos
    #parametro de entrada:
    #objeto sample
    def insert_sample(self, sample):
        session=self._get_session()
        session.add(sample)
        session.commit()
        session.close()
    #funcion que retorna el promedio de las ultimas 10 mediciones
    #retorna un objeto sample con el promedio de cada medida en sus atributos
    def get_average_sample(self):
        temp=0
        humedad=0
        presion=0
        viento=0
        #obtiene la sesion
        session=self._get_session()
        #obtiene 10 medidas ordenadas por id en forma descendente
        query = session.query(Samples).order_by(desc(Samples.id)).limit(10)
        samples = query.all()
        #suma los valores de las ultimas 10 medidas
        for s in samples:
            temp=temp+s.temperature
            humedad=humedad+s.humidity
            presion=presion+s.pressure
            viento=viento+s.windspeed
        average=Samples()
        #calcula el promedio
        average.temperature=float(temp)/10
        average.humidity=float(humedad)/10
        average.pressure=float(presion)/10
        average.windspeed=float(viento)/10
        session.close()
        #retorna el objeto
        return average