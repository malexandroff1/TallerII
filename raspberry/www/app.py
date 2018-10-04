# Imports
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from flask import make_response
from flask import session
import ConfigParser
import RPi.GPIO as GPIO

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


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
		return render_template('panel-control.html', form='',user=username)
	errors = {'Error' : 'You are not logged.'}
	return render_template('index.html', form=errors)

def validateFormLogin(form):
	form.errors = {}

	if len(form['username'].strip()) == 0:
		form.errors['username'] = 'Username can not be blank.'
	elif form['username'].isdigit():
		form.errors['username'] = 'Username can not be integer.' 
	elif: user != form['username']:
		form.errors['username'] = 'You not are register.'
	elif: password != form['password']:
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
	directory_config = './'
		
	if not os.path.exists(directory_config):
		logger_main.error('Error: Fail To Find Directory.')
		exit()

	path_config = directory_config + 'properties.cfg'

	Config = ConfigParser.ConfigParser() 
	Config.read(path_config) #ruta relativa /usr/lib 

	user = ConfigSectionMap("sessions")['username']
	password = ConfigSectionMap("session")['password']
	app.run(debug=True)
	#app.run(host='http://192.168.99.100', port=8888, debug=True)

