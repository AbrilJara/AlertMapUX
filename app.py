from flask import Flask
from flask_bootstrap import Bootstrap5
from flask import request
from flask import render_template
from flask import abort, redirect, url_for

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/configuracion")
def configuracion():
    return render_template('configuracion.html')

@app.route("/mapa")
def mapa():
    return render_template('mapa.html')

@app.route("/alertas")
def alertas():
    return render_template('alertas.html')

@app.route("/informacion")
def informacion():
    return render_template('informacion.html')
