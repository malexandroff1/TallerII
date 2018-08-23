from database import Database
from models import Samples
import time
from random import randint

db=Database()
session=db.get_session()
while True:
	sample=Samples()
	sample.temperature=	randint(0, 100)
	sample.humidity=randint(0, 100)
	sample.pressure=randint(900, 1024)
	sample.windspeed=randint(25, 500)
	session.add(sample)
	session.commit()
	time.sleep(1)
session.close()
