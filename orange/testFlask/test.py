from flask import Flask
app = Flask(__name__)

@app.route("/")
def test():
    return "Esto es una prueba de servidor Flask"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8800, debug=True)
