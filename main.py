from flask import Flask, render_template, request, jsonify
from replit import db
import random
from google.oauth2 import id_token
from google.auth.transport import requests
from static.db.entities import consejo, tarea, categoria

from static.api.categoria import categoria_blueprint
from static.api.consejo import consejo_blueprint
from static.api.diario import diario_blueprint
from static.api.tarea import tarea_blueprint
from static.api.timer import timer_blueprint
from static.api.usuario import usuario_blueprint

#from static.db import crear_tablas

app = Flask(__name__)

app.register_blueprint(categoria_blueprint)
app.register_blueprint(consejo_blueprint)
app.register_blueprint(diario_blueprint)
app.register_blueprint(tarea_blueprint)
app.register_blueprint(timer_blueprint)
app.register_blueprint(usuario_blueprint)

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]


@app.route('/', methods=['GET'])
def index():
  consejos = consejo.getall()
  consejo_random = consejos[random.randint(0, len(consejos)-1)][1]
  return render_template('index.html', consejo=consejo_random)

@app.route('/home', methods=['POST'])
def home():
  data = request.get_json()
  usuario_id = get_userid(data['token'])
  consejos = consejo.getall()
  consejo_random = consejos[random.randint(0, len(consejos)-1)][1]
  tareas_recurrentes = tarea.recurrente_getall(usuario_id)
  tareas_no_recurrentes = tarea.no_recurrente_getall(usuario_id)
  categorias = categoria.getall(usuario_id)
  
  return render_template('home.html', consejo=consejo_random, tareas_recurrentes=tareas_recurrentes, tareas_no_recurrentes=tareas_no_recurrentes, categorias=categorias)

@app.route('/pomodoro', methods=['GET', 'POST'])
def pomodoro():
  return render_template('pomodoro.html')

@app.route('/configuracion', methods=['GET', 'POST'])
def configuracion():
  return render_template('configuracion.html')

@app.route('/welcome', methods=['GET', 'POST'])
def bienvenida():
  return render_template('bienvenida.html')
  



def get_userid(token):
  try:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), None)
    userid = idinfo['sub']
  except ValueError:
    return False
  return userid



db["cantidad_tarea"] = 1




app.run(host='0.0.0.0', port=8080)