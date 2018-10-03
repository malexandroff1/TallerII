# Imports
from aux_pro import Process
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from database import Database
from models import Samples
from getMetrics import _get_metrics 
from flask import make_response
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

###*
#Numeros posibles para el muestreo NO TOCAR
numbers = [0 , 1000, 2000, 5000, 10000, 30000, 60000]

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   2 : {'name' : 'Control 1', 'state' : GPIO.LOW},
   3 : {'name' : 'Control 2', 'state' : GPIO.LOW},
   4 : {'name' : 'Control 3', 'state' : GPIO.LOW},
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

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

	#OBTENER EL UTILMO ESTADO
	

	return render_template('index.html', form=pins)

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
            led = int(request.form['led'])
            state = request.form['state']
                if state == 'ON':
                    GPIO.output(led, GPIO.HIGH)
                else:
                    GPIO.output(led, GPIO.LOW)

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

