#!/usr/bin/python

import os
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from flask import make_response
from flask import session
import configparser
import RPi.GPIO as GPIO
import database
import models

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = database.Database()

directory_config = './'

path_config = directory_config + 'properties.cfg'

config = configparser.ConfigParser()
config.read(path_config)

user = config.get('sessions', 'username')
password = config.get('sessions','password')


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


pin_2 = models.Pin()
pin_2.pin = 2

pin_3 = models.Pin()
pin_3.pin = 3

pin_4 = models.Pin()
pin_4.pin = 4

pin_2 = db.get_pin(pin_2)
pin_3 = db.get_pin(pin_3)
pin_4 = db.get_pin(pin_4)

pines = []

pines.append(pin_2)
pines.append(pin_3)
pines.append(pin_4)


# Set each pin as an output and make it low:

for p in range(len(pines)):
   GPIO.setup(pines[p].pin, GPIO.OUT)
   GPIO.output(pines[p].pin, GPIO.LOW)
   pines[p].state = "OFF"
   db.update_pin(pines[p])


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   session.pop('password', None)
   session.clear()
   return redirect(url_for('index'))

@app.route('/login', methods = ['POST'])
def login():
	if request.method == 'POST':
		if validateFormLogin(request.form):
			session['username'] = request.form['username']
			session['password'] = request.form['password']
			return redirect(url_for('panel_control'))
	return render_template('index.html', form=request.form)


@app.route('/panel-control')
def panel_control(form):
    data = []
    selects = []
    if 'username' in session:
        username = session['username']
		for p in range(len(pines)):
	    	pines[p] = db.get_pin(pines[p])
            data.append({'pin' : str(pines[p].pin), 'state' : str(pines[p].state)})
            if pines[p].state == 'ON':
                selects.append({'pin' : str(pines[p].pin),'choose' : '','on' : 'selected', 'off' : ''})
            else:
                selects.append({'pin' : str(pines[p].pin),'choose' : 'selected','' : '', 'off' : 'selected'})
        json_string = json.dumps(data)
		return render_template('panel_control.html', form=data, user=username, selects=selects)
    errors = {'Error' : 'You are not logged.'}
    return render_template('index.html', form=errors)

def validateFormLogin(form):
	form.errors = {}

	if len(form['username'].strip()) == 0:
		form.errors['username'] = 'Username can not be blank.'
	elif form['username'].isdigit():
		form.errors['username'] = 'Username can not be integer.' 
	elif user != form['username']:
		form.errors['username'] = 'You not are register.'
	elif password != form['password']:
		form.errors['password'] = 'Your password falied.'

	if len(form['password'].strip()) == 0:
		form.errors['password'] = 'Password can not be blank.'
	return len(form.errors) == 0


###*
#NO TOCAR
def validate_form(form):
    form.errors = {}
    if len(form['led1'].strip()) == 0:
        form.errors['led1'] = 'Led can not be blank.'

    if len(form['led2'].strip()) == 0:
    	form.errors['led2'] = 'State can not be blank.'

    if len(form['led2'].strip()) == 0:
    	form.errors['led2'] = 'State can not be blank.'

    return len(form.errors) == 0


###*
#Cuando se ejecuta /index se redirige a la pagina index.html
@app.route('/')
def index():
	return render_template('index.html',form='')

@app.route('/index')
def index2():
	return render_template('index.html',form='')

@app.route('/controler',methods = ['POST'])
def controler():
	if request.method == 'POST' and 'username' in session:
		valid = validate_form(request.form)
		if valid:
			led_states = []
            led_states.append(request.form['led1'])
		    led_states.append(request.form['led2'])
		    led_states.append(request.form['led3'])
           	pos = 0
            for p in range(len(pines)):
            	if led_states[p] == "ON":
            	   	GPIO.output(pines[p],GPIO.HIGH)
            	   	db.update_pin(pines[p])
            	else:
            		GPIO.output(pines[p], GPIO.LOW)
            		db.update_pin(pines[p])
		    
		    return json.dumps({'http': 200})
		form = request.form
	return render_template('error.html', form='')


###*
#Si se ejecuta este archivo el main se toma en cuenta, sino no.
if __name__ == "__main__":
		
        app.run(debug=True)
	#app.run(host='http://192.168.99.100', port=8888, debug=True)

