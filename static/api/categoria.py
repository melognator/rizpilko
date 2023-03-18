from flask import Blueprint, request, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests
from ..db.entities import categoria

categoria_blueprint = Blueprint('categoria', __name__,template_folder='')

# categorias

@categoria_blueprint.route('/categorias/create', methods=['POST'])
def categoria_create(usuario_id):
  datos_categoria = request.get_json()
  if 'nombre' in datos_categoria:
    categoria.create(usuario_id, datos_categoria['nombre'])
    return 'Categoria registrada', 200
  else:
    return 'Nombre requerido', 200

@categoria_blueprint.route('/categorias', methods=['POST'])
def catgoria_getall():
  data = request.get_json()
  usuario_id = get_userid(data['token'])
  categorias = categoria.getall(usuario_id)
  # for fila in tablas:
  #   html += f"""
  #   <p>ID: {fila[0]}</p>
  #   <p>Usuario: {fila[1]}</p>
  #   <p>Nombre: {fila[2]}</p>
  #   <hr>
  #   """
  # return html, 200

  return jsonify(categorias)

@categoria_blueprint.route('/usuario/<int:usuario_id>/categorias/<int:categoria_id>', methods=['GET'])
def categoria_get(usuario_id, categoria_id):
  fila_categoria = categoria.get(categoria_id)[0]
  html = f"""
    <p>ID: {fila_categoria[0]}</p>
    <p>Usuario: {fila_categoria[1]}</p>
    <p>Nombre: {fila_categoria[2]}</p>
    <hr>
  """
  return html, 200

@categoria_blueprint.route('/usuario/<int:usuario_id>/categorias/<int:categoria_id>', methods=['PUT'])
def categoria_update(usuario_id, categoria_id):
  datos_categoria = request.get_json()
  if 'nombre' in datos_categoria:
    categoria.update(categoria_id, datos_categoria['nombre'])
    return 'Categoria actualizada', 200
  else:
    return 'Nombre requerido', 422

@categoria_blueprint.route('/usuario/<int:usuario_id>/categorias/<int:categoria_id>', methods=['DELETE'])
def categoria_delete(usuario_id, categoria_id):
  categoria.delete(categoria_id)
  return 'Categoria borrada', 200


def get_userid(token):
  try:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), None)
    userid = idinfo['sub']
  except ValueError:
    return False
  return userid