# Imports
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from random import randint
from aux_pro import Process
from database import Database
from models import Samples
import json

pro = Process()

###*
#Genera los objetos Samples y arma un JSON que se retorna al ejecutar la funcion.
def _get_metrics():

	pro.start_process()
	average=Samples()
	last_meas=Samples()
	
	
	db=Database()
	last_meas = db.get_last_sample()
	average = db.get_average_sample()
	
	
	###
	#COMENTAR O BORRAR DE ACA
	'''
	average.temperature = randint(0, 100)
	average.humidity = randint(0, 100)
	average.pressure = randint(900, 1024)
	average.windspeed = randint(25, 500)
	last_meas.temperature = randint(0, 100)
	last_meas.humidity = randint(0, 100)
	last_meas.pressure = randint(900, 1024)
	last_meas.windspeed = randint(25, 500)
	'''
	###*
	#HASTA ACA

	###*
	#Se crea un conjunto clave,valor para luego crear el json
	test = [
		{ "temp" : last_meas.temperature,"hum" : last_meas.humidity,"pre" : last_meas.pressure, "wind": last_meas.windspeed},
		{ "temp" : average.temperature,"hum" : average.humidity,"pre" : average.pressure, "wind": average.windspeed}
		
	]

	###*
	#Creamos el json
	test = json.dumps(test)

	return test

	