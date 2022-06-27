from operator import invert
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():

    if 'primera_vez' in request.cookies:
        return render_template('index.html')
    else:
        response = make_response(render_template('index.html'))
        response.set_cookie('primera_vez', 'true')
        response.set_cookie('invert_color', 'false')
        response.set_cookie('tamanio_texto', '0')
        return response

    

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
