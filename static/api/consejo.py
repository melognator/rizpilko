from flask import Blueprint, request, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests
from ..db.entities import consejo

consejo_blueprint = Blueprint('consejo', __name__,template_folder='')

# consejos

@consejo_blueprint.route('/consejos', methods=['GET'])
def consejo_getall():
  tablas = consejo.getall()
  html = f"""
  <h1>Consejos</h1>
  """

  for fila in tablas:
    html += f"""
    <p>ID: {fila[0]}</p>
    <p>Contenido: {fila[1]}</p>
    <hr>
    """
  return html, 200

@consejo_blueprint.route('/consejos', methods=['POST'])
def consejo_create():
  datos_consejo = request.get_json()
  if 'contenido' in datos_consejo:
    consejo.create(datos_consejo['contenido'])
    return 'Consejo creado', 200
  else:
    return 'Contenido requerido', 422

@consejo_blueprint.route('/consejos/<int:id_consejo>', methods=['GET'])
def consejo_get(id_consejo):
  fila_consejo = consejo.get(id_consejo)[0]
  html = f"""
    <p>ID: {fila_consejo[0]}</p>
    <p>Contenido: {fila_consejo[1]}</p>
    <hr>
  """
  return html, 200

@consejo_blueprint.route('/consejos/<int:id_consejo>', methods=['PUT'])
def consejo_update(id_consejo):
  datos_consejo = request.get_json()
  if 'contenido' in datos_consejo:
    consejo.cambiar_contenido(id_consejo, datos_consejo['contenido'])
    return 'Consejo actualizado', 200
  else:
    return 'Contenido requerido', 422

@consejo_blueprint.route('/consejos/<int:id_consejo>', methods=['DELETE'])
def consejo_delete(id_consejo):
  consejo.delete(id_consejo)
  return 'Consejo borrado', 200


def get_userid(token):
  try:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), None)
    userid = idinfo['sub']
  except ValueError:
    return False
  return userid