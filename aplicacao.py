from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:021092@localhost/equipes'
db = SQLAlchemy(app)


class equipes(db.Model):
    __tablename__="clube"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45))
    cores = db.Column(db.String(45))
    estadio = db.Column(db.String(45))
    def __init__(self, nome, cores, estadio):
        self.nome = nome
        self.cores = cores
        self.estadio = estadio
    




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

@app.route("/cadastro")
def cadastrar_equipe():
    return render_template("cadastro.html")


app.run()
