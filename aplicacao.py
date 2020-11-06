from flask import Flask
from flask import render_template


app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/palmeiras.html")
def palmeiras():
    return render_template("palmeiras.html")
@app.route("/liverpool.html")
def liverpool():
    return render_template("liverpool.html")
@app.route("/milan.html")
def milan():
    return render_template("milan.html")
@app.route("/paysandu.html")
def paysandu():
    return render_template("paysandu.html")
@app.route("/portuguesa.html")
def portuguesa():
    return render_template("portuguesa.html")
@app.route("/chelsea.html")
def chelsea():
    return render_template("chelsea.html")
@app.route("/index.html")
def resultado():
    return render_template("index.html")
app.run()
