# Imports
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json
from database import Database
from models import Samples

app = Flask(__name__)

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

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		#a = request.form['period']

		#"[{&#34;hum&#34;: 56.4, &#34;pre&#34;: 951.7, &#34;temp&#34;: 43.1, &#34;wind&#34;: 298.9}, {&#34;hum&#34;: 38, &#34;pre&#34;: 901, &#34;temp&#34;: 21, &#34;wind&#34;: 245}]"
		
		db=Database()
		last_meas = db.get_last_sample()
		average = db.get_average_sample()

		test = [
			{ "temp" : average.temperature,"hum" : average.humidity,"pre" : average.pressure, "wind": average.windspeed},
			{ "temp" : last_meas.temperature,"hum" : last_meas.humidity,"pre" : last_meas.pressure, "wind": last_meas.windspeed}
		]
		#test = [name=1,2,3,4,5,6]
		test = json.dumps(test)
		return render_template('result.html', test=test)
	else:
		return render_template('result.html')


if __name__ == "__main__":
    app.run(host='192.168.99.100', port=8888)
    #app.run(host='192.168.99.100', port=8888)

