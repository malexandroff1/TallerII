# Imports
from flask import redirect, url_for, request, render_template, Flask
from flask import jsonify
from flask import json

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
		a = request.form['period']
		jsonStr = json.dumps(a)
		return jsonify(result=jsonStr)
	else:
		return render_template("result.html")


if __name__ == "__main__":
    app.run(host='192.168.99.100', port=8888)

