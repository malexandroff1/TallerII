from database import Database
from models import Samples
import time
from random import randint

db=Database()
while True:
	sample=Samples()
	sample.temperature=	randint(0, 100)
	sample.humidity=randint(0, 100)
	sample.pressure=randint(900, 1024)
	sample.windspeed=randint(25, 500)
	db.insert_sample(sample)
	time.sleep(1)
