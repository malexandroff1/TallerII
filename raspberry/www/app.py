# Imports
from aux_pro import Process
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from database import Database
from models import Samples
from getMetrics import _get_metrics 
from flask import make_response
from handlerGPIO import trafficLIGHTS
 
###*
#Numeros posibles para el muestreo NO TOCAR
numbers = [0 , 1000, 2000, 5000, 10000, 30000, 60000]

###*
#NO TOCAR
def validate_form(form):
    form.errors = {}
    if len(form['led'].strip()) == 0:
        form.errors['led'] = 'Led can not be blank.'

    if len(form['state'].strip()) == 0:
    	form.errors['state'] = 'State can not be blank.'

    return len(form.errors) == 0


app = Flask(__name__)
pro = Process()

###*
#Cuando se ejecuta /index se redirige a la pagina index.html
@app.route('/')
def index():
	form = {'period': ''}

	#OBTENER EL UTILMO ESTADO
	

	return render_template('index.html', form=form)

@app.route('/index')
def index2():
	form = {'period': ''}

	#OBTENER EL UTILMO ESTADO
	
	return render_template('index.html', form=form)

@app.route('/controler',methods = ['POST'])
def controler():
	if request.method == 'POST':
		valid = validate_form(request.form)
		if valid:
			led = request.form['led']
			state = request.form['state']
			return json.dumps({'led': led, 'state' : state})
		form = request.form
		return render_template('index.html', form=form)

	#HACER LLAMADA A LA RASPBERRY
	#FUNCIONES
	


	#return json.dumps({'led': led, 'state' : state})


###*
#Si se ejecuta este archivo el main se toma en cuenta, sino no.
if __name__ == "__main__":
	app.run(host='http://192.168.99.100', port=8888)
	#app.run(host='http://localhost', port=8888)

