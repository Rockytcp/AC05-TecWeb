from flask import Flask
from flask import render_template, request, url_for, redirect, g
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

class partidas(db.Model):
    __tablename__="partidas"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mandante = db.Column(db.String(45))
    visitante = db.Column(db.String(45))
    estadio = db.Column(db.String(45))
    placar = db.Column(db.String(5))
    def __init__(self, mandante, visitante, estadio, placar):
        self.mandante = mandante
        self.visitante = visitante
        self.estadio = estadio
        self.placar = placar

db.create_all()
    

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

@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")

@app.route("/cadastro_rodada")
def cadastrar_rodada():
    return render_template("cadastro_rodada.html")

@app.route("/visualizar_clubes.html")
def visualizar_clubes():
    return render_template("visualizar_clubes.html")

@app.route("/registrar_partida", methods=['GET', 'POST'])
def registrar_partida():
    if request.method == 'POST':
        mandante = (request.form.get("mandante"))
        visitante = (request.form.get("visitante"))
        estadio = (request.form.get("estadio"))
        placar = (request.form.get("placar"))
        if mandante:
            var = partidas(mandante, visitante, estadio, placar)
            db.session.add(var)
            db.session.commit()
    return redirect(url_for("mensagem"))


@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = (request.form.get("nome"))
        cores = (request.form.get("cores"))
        estadio = (request.form.get("estadio"))
        if nome:
            var = equipes(nome, cores, estadio)
            db.session.add(var)
            db.session.commit()
    return redirect(url_for("mensagem"))
    

@app.route("/lista")
def lista():
    times = equipes.query.all()
    return render_template("lista.html", times=times)


app.run()
