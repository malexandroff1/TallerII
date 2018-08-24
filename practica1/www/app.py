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

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/result.html',methods = ['POST', 'GET'])
def result():
	
	pro.start_process()
	average=Samples()
	last_meas=Samples()
	
	'''
	db=Database()
	last_meas = db.get_last_sample()
	average = db.get_average_sample()
	'''

	period = 0
	average.temperature = 56.4
	average.humidity = 951.7
	average.pressure = 43.1
	average.windspeed = 298.9
	last_meas.temperature = 21
	last_meas.humidity = 38
	last_meas.pressure = 901
	last_meas.windspeed = 245

	test = [
		{ "temp" : average.temperature,"hum" : average.humidity,"pre" : average.pressure, "wind": average.windspeed},
		{ "temp" : last_meas.temperature,"hum" : last_meas.humidity,"pre" : last_meas.pressure, "wind": last_meas.windspeed}
	]
	
	test = json.dumps(test)


	if request.method == 'POST':
		period = request.form['period']
	else:
		period = request.args.get('period')

	return render_template('result.html', test=test,reload=period)

if __name__ == "__main__":
    app.run(host='198.', port=8888)
    #app.run(host='http://localhost', port=8888)

