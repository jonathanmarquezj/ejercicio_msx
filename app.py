import os
from flask import Flask, render_template, abort, request
import json

app = Flask(__name__)

with open("MSX.json") as fichero:
	lista_juegos_msx=json.load(fichero)

#INICIO
@app.route('/', methods=["GET"])
def inicio():
	return render_template("inicio.html")

#PARA BUSCAR JUEGOS
@app.route('/juegos', methods=["GET", "POST"])
def juegos():
	return render_template("juegos.html")

#PARA LISTAR LOS JUEGOS ENCONTADOS
@app.route('/listajuegos', methods=["GET", "POST"])
def listajuegos():
	if request.method == "POST":
		juego=request.form['juego'] #Para guardar la busqueda en una variable
		#Realiza la busqueda en el listado de los juegos.
		busqueda=[obj for obj in lista_juegos_msx if(str(obj['nombre']).find(juego) == 0)]

		return render_template("listajuegos.html", juego=juego, lista_juegos=busqueda)
	else:
		return render_template("listajuegos.html", juego="todo", lista_juegos=lista_juegos_msx)

# Tienes que crear esta variable si no la tienes, en heroku no hace falta.
# Ponemos en el terminal para poner el puerto en nustra maquina local el siguiente comando.
#   $ export PORT=8080
port=os.environ["PORT"]

app.run('0.0.0.0', int(port), debug=True)
