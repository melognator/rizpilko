import os
from flask import Blueprint, request, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests
from ..db.entities import usuario, categoria

usuario_blueprint = Blueprint('usuario', __name__,template_folder='')

#usuario

@usuario_blueprint.route('/usuario', methods=['GET'])
def usuario_getall():
  data = request.get_json()
  if 'adminpass' in data:
    if data['adminpass'] == os.environ['adminpass']:
      return jsonify(usuario.getall()), 200
  return 'Acceso denegado', 403

# @usuario_blueprint.route('/crear-usuario', methods=['POST'])
# def usuario_create():
#   data = request.get_json()
#   if 'id' in data and 'nombre' in data:
#     usuario.create(data['id'], data['nombre'])
#     return 'Usuario creado', 200
#   return 'Id requerido', 422

@usuario_blueprint.route('/auth', methods=['POST'])
def auth():
  data = request.get_json()
  userid = get_userid(data['token'])
  if userid:
    usr = usuario.get(userid)
    if len(usr) == 0:
      usuario.create(userid, data['nombre'].split()[0])

      # temp
      categorias = ["Personal", "Trabajo", "Estudios", "Ocio", "Social", "Salud", "Finanzas", "Espiritual", "Otro"]
      for categ in categorias:
        categoria.create(userid, categ)

    return 'Autorizado', 200
  else:
    return 'No autorizado', 401

@usuario_blueprint.route('/usuario/<int:usuario_id>', methods=['DELETE'])
def usuario_delete(usuario_id):
  data = request.get_json()
  if 'adminpass' in data:
    if data['adminpass'] == os.environ['adminpass']:
      usuario.delete(usuario_id)
      return 'Usuario borrado', 200
  return 'Acceso denegado', 403
  
@usuario_blueprint.route('/usuario', methods=['POST'])
def usuario_get():
  data = request.get_json()
  usuario_id = get_userid(data['token'])
  user = usuario.get(usuario_id)
  return jsonify(user), 200

# tabla_usuario = '''
# CREATE TABLE Usuario(
# ID INTEGER NOT NULL,
# login TEXT NOT NULL,
# password TEXT NOT NULL,
# codigo_recuperacion TEXT NOT NULL,
# nombre TEXT,
# experiencia INTEGER DEFAULT 0,
# PRIMARY KEY (ID)
# );
# '''

@usuario_blueprint.route('/usuario/incrementar-xp', methods=['POST'])
def usuario_incrementar_exp():
  data = request.get_json()
  usuario_id = get_userid(data['token'])
  usuario.incrementar_exp(usuario_id, data['xp'])
  return 'Hecho', 200

@usuario_blueprint.route('/usuario/<int:id_usuario>/cambiar_nombre', methods=['PUT'])
def usuario_cambiar_nombre(id_usuario):
  data = request.get_json()
  if 'adminpass' in data:
    if data['adminpass'] == os.environ['adminpass']:
      usuario.cambiar_nombre(id_usuario, data['nombre'])
      return f"Se ha cambiado el nombre a {data['nombre']}", 200
  return 'Acceso denegado', 403



def get_userid(token):
  try:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), None)
    userid = idinfo['sub']
  except ValueError:
    return False
  return userid
