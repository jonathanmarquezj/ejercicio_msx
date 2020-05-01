import os
from flask import Flask, render_template, abort, request
import json

app = Flask(__name__)

with open("MSX.json") as fichero:
	lista_juegos_msx=json.load(fichero)

#PARA PERSONALIZAR EL ERROR 404
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>ERROR: 404</h1><br/>página no encontrada <br/><br/><a href='/juegos'>Atras</a>"

#INICIO
@app.route('/', methods=["GET"])
def inicio():
	return render_template("inicio.html")


#PARA BUSCAR JUEGOS
@app.route('/juegos', methods=["GET", "POST"])
@app.route('/juegos/<detalle>', methods=["GET", "POST"])
def juegos(detalle=None):
	#PARA PASAR DE UNA PAGINA A OTRA
	estado="juegos"
	buscar=""
	if request.method == "POST":
		estado=request.form['estado']
		buscar=request.form['buscador']

	if estado == "juegos":
		if detalle:
			detalle=[obj for obj in lista_juegos_msx if(obj['id'] == int(detalle))]
			if not detalle:
				abort(404)
		return render_template("juegos.html", detalle=detalle, estado=estado, buscar=buscar)
	else:
		juego=request.form['juego'] #Para guardar la busqueda en una variable
		#Realiza la busqueda en el listado de los juegos.
		busqueda=[obj for obj in lista_juegos_msx if(str(obj['nombre']).find(juego) == 0)]

		return render_template("juegos.html", juego=juego, lista_juegos=busqueda, estado="lista_juegos")



# Tienes que crear esta variable si no la tienes, en heroku no hace falta.
# Ponemos en el terminal para poner el puerto en nustra maquina local el siguiente comando.
#   $ export PORT=8080
port=os.environ["PORT"]

app.run('0.0.0.0', int(port), debug=True)
