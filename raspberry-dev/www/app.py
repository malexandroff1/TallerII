
import os
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from flask import make_response
from flask import session
import database
import models

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

user = 'admin'
password = 'admin'


db = database.Database()
pin_2 = models.Pin()
pin_2.pin = 2

pin_3 = models.Pin()
pin_3.pin = 3

pin_4 = models.Pin()
pin_4.pin = 4

pin_2 = db.get_pin(pin_2)
pin_3 = db.get_pin(pin_3)
pin_4 = db.get_pin(pin_4)

pins = {
   pin_2.pin : {'name' : pin_2.pin, 'state' : pin_2.state},
   pin_3.pin : {'name' : pin_3.pin, 'state' : pin_3.state},
   pin_4.pin : {'name' : pin_4.pin, 'state' : pin_4.state}
}


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   session.pop('password', None)
   return redirect(url_for('index'))

@app.route('/login', methods = ['POST'])
def login():
	if request.method == 'POST':
		if validateFormLogin(request.form):
			session['username'] = request.form['username']
			session['password'] = request.form['password']
			return redirect(url_for('panelControl'))
	return render_template('index.html', form=request.form)


@app.route('/panel-control')
def panelControl():
	if 'username' in session:
		username = session['username']
		return render_template('panel-control.html', form=pins,user=username)
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
    if len(form['led'].strip()) == 0:
        form.errors['led'] = 'Led can not be blank.'

    if len(form['state'].strip()) == 0:
    	form.errors['state'] = 'State can not be blank.'

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
	if request.method == 'POST':
		valid = validate_form(request.form)
		if valid:
			led = int(request.form['led'])
			state = request.form['state']

			return json.dumps({'http': 200})
		form = request.form
		return render_template('error.html', form='')


###*
#Si se ejecuta este archivo el main se toma en cuenta, sino no.
if __name__ == "__main__":
	app.run(debug=True)

