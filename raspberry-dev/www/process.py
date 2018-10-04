from database import Database
from models import Samples
import time
from random import randint
#crea una instancia del objeto Database
db=Database()
while True:
	#crea una instancia de una medida
	sample=Samples()
	#crea las medidas en forma aleatoria
	sample.temperature=	randint(0, 100)
	sample.humidity=randint(0, 100)
	sample.pressure=randint(900, 1024)
	sample.windspeed=randint(25, 500)
	#inserta la nueva muestra en la base de datos
	db.insert_sample(sample)
	time.sleep(1)
