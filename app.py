import os
from flask import Flask, render_template, abort, request
import json

app = Flask(__name__)

with open("MSX.json") as fichero:
	lista_juegos_msx=json.load(fichero)

#INICIO
@app.route('/', methods=["GET", "POST"])
def inicio():
	return render_template("inicio.html")

#PARA BUSCAR JUEGOS
@app.route('/juegos', methods=["GET", "POST"])
def juegos():
	return render_template("juegos.html")

#PARA LISTAR LOS JUEGOS ENCONTADOS
@app.route('/listajuegos', methods=['GET', "POST"])
def listajuegos():
	if request.method == 'POST': #Si tiene POST
		return render_template("listajuegos.html", lista_juegos_msx=lista_juegos_msx)
	else: #En caso de que no tenga POST
		abort(404)


# Tienes que crear esta variable si no la tienes, en heroku no hace falta.
# Ponemos en el terminal para poner el puerto en nustra maquina local el siguiente comando.
#   $ export PORT=8080
port=os.environ["PORT"]

app.run('0.0.0.0', int(port), debug=True)
