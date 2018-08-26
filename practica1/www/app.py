# Imports
from aux_pro import Process
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from database import Database
from models import Samples
from getMetrics import _get_metrics 


app = Flask(__name__)
pro = Process()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index2')
def index2():
	return render_template('index.html')

###*
#Funcion que ejecuta el metodo _get_metrics()
#Return: esta funcion devuelve un JSON con los datos obtenidos de la BBD
#No cambia de pagina
@app.route('/metricas',methods = ['POST', 'GET'])
def metricas():
	values = _get_metrics()
	return values

###*
#
@app.route('/metrics.html',methods = ['POST', 'GET'])
def metrics():

	###*
	#Valor del periodo para recargar la pagina
	period = 0

	values = _get_metrics()

	###*
	#Si el método del formulario es POST o GET se obtiene el periodo.
	if request.method == 'POST':
		period = request.form['period']
	else:
		if request.method == 'GET':
			period = request.args.get('period')

	###*
	#Redirigimos al sitio metrics.html y le enviamos las variables test y reload
	return render_template('metrics.html', test=values,reload=period)

###*
#Si se ejecuta este archivo el main se toma en cuenta, sino no.
if __name__ == "__main__":
	app.run(host='http://192.168.99.100', port=8888)
	#app.run(host='http://localhost', port=8888)

