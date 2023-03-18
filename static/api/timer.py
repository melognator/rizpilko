from flask import Blueprint, request, jsonify, render_template
from google.oauth2 import id_token
from google.auth.transport import requests
from ..db.entities import actividad, categoria

from datetime import datetime

timer_blueprint = Blueprint('timer', __name__,template_folder='')

# actividades / timer

@timer_blueprint.route('/temporizador', methods=['GET', 'POST'])
def actividad_getall():
  data = request.get_json()
  
  usuario_id = get_userid(data['token'])
  actividades = actividad.getall(usuario_id)
  categorias = categoria.getall(usuario_id)
  return render_template('temporizador.html', actividades=actividades, datetime=datetime, categorias = categorias)

  # for fila_actividad in tablas:
  #   html += f"""
  #   <p>ID: {fila_actividad[0]}</p>
  #   <p>Usuario: {fila_actividad[1]}</p>
  #   <p>Categoría: {fila_actividad[2]}</p>
  #   <p>Título: {fila_actividad[3]}</p>
  #   <p>Fecha comienzo: {fila_actividad[4]}</p>
  #   <p>Fecha fin: {fila_actividad[5]}</p>
  #   <hr>
  #   """

@timer_blueprint.route('/temporizador/create', methods=['POST'])
def actividad_create():
  
  data = request.get_json()
  usuario_id = get_userid(data['token'])

  if 'categoria' in data:
    categoria_id = data['categoria']
  else:
    categoria_id = 0
  
  if 'titulo' in data and 'fecha_comienzo' in data and 'fecha_fin' in data:
    actividad.create(usuario_id, categoria_id, data['titulo'], data['fecha_comienzo'], data['fecha_fin'])

    return 'Actividad registrada', 200
  else:
    return 'Faltan datos', 422

@timer_blueprint.route('/usuario/<int:usuario_id>/timer/<int:actividad_id>', methods=['GET'])
def actividad_get(usuario_id, actividad_id):
  fila_actividad = actividad.get(actividad_id)[0]
  html = f"""
    <p>ID: {fila_actividad[0]}</p>
    <p>Usuario: {fila_actividad[1]}</p>
    <p>Categoría: {fila_actividad[2]}</p>
    <p>Título: {fila_actividad[3]}</p>
    <p>Fecha comienzo: {fila_actividad[4]}</p>
    <p>Fecha fin: {fila_actividad[5]}</p>
    <hr>
  """
  return html, 200

@timer_blueprint.route('/usuario/<int:usuario_id>/timer/<int:actividad_id>', methods=['PUT'])
def actividad_update(usuario_id, actividad_id):
  datos_actividad = request.get_json()
  # formato para las fechas: "%d/%m/%Y %H:%M:%S"
  if 'categoria' in datos_actividad:
    categoria_id = datos_actividad['categoria']
  else:
    categoria_id = 0

  if 'titulo' in datos_actividad and 'fecha_comienzo' in datos_actividad and 'fecha_fin' in datos_actividad:
    actividad.update(actividad_id, categoria_id, datos_actividad['titulo'], datos_actividad['fecha_comienzo'], datos_actividad['fecha_fin'])
    return 'Actividad actualizada', 200
  else:
    return 'Faltan datos', 422

@timer_blueprint.route('/temporizador', methods=['DELETE'])
def actividad_delete():
  data = request.get_json()

  actividad.delete(data['actividad_id'])
  return 'Actividad borrada', 200


def get_userid(token):
  try:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), None)
    userid = idinfo['sub']
  except ValueError:
    return False
  return userid