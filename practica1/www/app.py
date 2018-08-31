# Imports
from aux_pro import Process
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from database import Database
from models import Samples
from getMetrics import _get_metrics 
 
numbers = [0 , 1000, 2000, 5000, 10000, 30000, 60000]


def validate_movie_data(form):
    form.errors = {}

    if len(form['period'].strip()) == 0:
        form.errors['period'] = 'Period can not be blank.'
    elif not form['period'].isdigit():
    	form.errors['period'] = 'Period can not be string.' 
    else:
    	ok = False
    	array_length = len(numbers)
    	for i in range(array_length):
    		if numbers[i] == int(form['period']):
    			ok = True
    	if not ok :
    		form.errors['period'] = 'Period can be between correct values.'

    return len(form.errors) == 0


app = Flask(__name__)
pro = Process()

###*
#Cuando se ejecuta /index se redirige a la pagina index.html
@app.route('/')
def index():
	form = {'period': ''}
	return render_template('index.html', form=form)

###*
#Cuando se ejecuta /index2 se regirige a la pagina index.html
@app.route('/index2')
def index2():
	form = {'period': ''}
	return render_template('index.html', form=form)

###*
#Funcion que ejecuta el metodo _get_metrics()
#Return: esta funcion devuelve un JSON con los datos obtenidos de la BBD
#No cambia de pagina
@app.route('/metricas',methods = ['POST', 'GET'])
def metricas():
	values = _get_metrics()
	return values

###*
#Cuando se ejecuta metrics.html se redirige a la página metrics.html
#Si se envian datos a este sitio por POST o GET la pagina metrics.html
#es la encargada de recibirlos.
@app.route('/metrics.html',methods = ['POST', 'GET'])
def metrics():

	###*
	#Valor del periodo para recargar la pagina
	period = 0

	###*
	#Obtiene un JSON con los promedios y ultimas medidas.
	values = _get_metrics()

	###*
	#Si el método del formulario es POST o GET se obtiene el periodo.
	#Si se envian parametros por la URL tambien se obtiene los datos
	if request.method == 'POST':
		valid = validate_movie_data(request.form)
		if valid:
			period = request.form['period']
			return render_template('metrics.html', test=values, reload=period)
		form = request.form
		return render_template('index.html', form=form)
	return render_template('metrics.html', test=values, reload=period)

###*
#Si se ejecuta este archivo el main se toma en cuenta, sino no.
if __name__ == "__main__":
	app.run(host='http://192.168.99.100', port=8888)
	#app.run(host='http://localhost', port=8888)

###*
#Redirigimos al sitio metrics.html y le enviamos las variables values y period