# Imports
from aux_pro import Process
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from database import Database
from models import Samples

app = Flask(__name__)
pro = Process()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index2')
def index2():
	return render_template('index.html')

@app.route('/metrics.html',methods = ['POST', 'GET'])
def metrics():
	
	pro.start_process()
	average=Samples()
	last_meas=Samples()
	
	'''
	db=Database()
	last_meas = db.get_last_sample()
	average = db.get_average_sample()
	'''

	###*
	#Valor del periodo para recargar la pagina
	period = 0

	###*
	#COMENTAR O BORRAR DE ACA
	average.temperature = 56.4
	average.humidity = 951.7
	average.pressure = 43.1
	average.windspeed = 298.9
	last_meas.temperature = 21
	last_meas.humidity = 38
	last_meas.pressure = 901
	last_meas.windspeed = 245
	###*
	#HASTA ACA

	###*
	#Se crea un conjunto clave,valor para luego crear el json
	test = [
		{ "temp" : average.temperature,"hum" : average.humidity,"pre" : average.pressure, "wind": average.windspeed},
		{ "temp" : last_meas.temperature,"hum" : last_meas.humidity,"pre" : last_meas.pressure, "wind": last_meas.windspeed}
	]
	
	###*
	#Creamos el json
	test = json.dumps(test)

	###*
	#Si el método del formulario es POST o GET se obtiene el periodo.
	if request.method == 'POST':
		period = request.form['period']
	else:
		if request.method == 'GET':
			period = request.args.get('period')

	###*
	#Redirigimos al sitio metrics.html y le enviamos las variables test y reload
	return render_template('metrics.html', test=test,reload=period)

###*
#Si se ejecuta este archivo el main se toma en cuenta, sino no.
if __name__ == "__main__":
	app.run(host='http://192.168.99.100', port=8888)
	#app.run(host='http://localhost', port=8888)

