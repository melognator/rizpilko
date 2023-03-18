from datetime import datetime
from flask import Blueprint, request, jsonify, render_template
from google.oauth2 import id_token
from google.auth.transport import requests
from ..db.entities import entrada

diario_blueprint = Blueprint('diario', __name__,template_folder='')

# entradas de diario


@diario_blueprint.route('/diario', methods=['GET', 'POST'])
def entrada_getall():
  data = request.get_json()
  usuario_id = get_userid(data['token'])
  entradas = entrada.getall(usuario_id)

  return render_template('diario.html', entradas=entradas, datetime=datetime)

  # for fila in tablas:
  #   html += f"""
  #   <p>ID: {fila[0]}</p>
  #   <p>Usuario: {fila[1]}</p>
  #   <p>Título: {fila[2]}</p>
  #   <p>Fecha modificación: {fila[3]}</p>
  #   <p>Contenido: {fila[4]}</p>
  #   <p>Categoría: {fila[5]}</p>
  #   <hr>
    # """

@diario_blueprint.route('/diario/create', methods=['POST'])
def entrada_create():
  data = request.get_json()
  fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  usuario_id = get_userid(data['token'])

  if 'contenido' in data:
    contenido = data['contenido']
  else:
    contenido = ''

  if 'categoria' in data:
    nombre_categoria = data['categoria']
  else:
    nombre_categoria = 'Diario personal'
  
  if 'titulo' in data:
    titulo = data['titulo']

    id_entrada = entrada.create(usuario_id, titulo, fecha_actual, contenido, nombre_categoria)
    return jsonify(id_entrada[0][0]), 200
  else:
    return 'Título requerido', 422

@diario_blueprint.route('/usuario/<int:usuario_id>/diario/<int:entrada_id>', methods=['GET'])
def entrada_get(usuario_id, entrada_id):
  fila_entrada = entrada.get(entrada_id)[0]
  html = f"""
    <p>ID: {fila_entrada[0]}</p>
    <p>Usuario: {fila_entrada[1]}</p>
    <p>Título: {fila_entrada[2]}</p>
    <p>Fecha modificación: {fila_entrada[3]}</p>
    <p>Contenido: {fila_entrada[4]}</p>
    <p>Categoría: {fila_entrada[5]}</p>
    <hr>
  """
  return html, 200

@diario_blueprint.route('/diario', methods=['PUT'])
def entrada_update():
  data = request.get_json()
  
  usuario_id = get_userid(data['token'])
  entrada_id = data['entrada_id']

  tabla_entrada = entrada.get(entrada_id)
  if len(tabla_entrada) > 0:
    if tabla_entrada[0][1] != usuario_id:
      return 'Acceso denegado', 403
  if len(tabla_entrada) == 0:
    return 'Acceso denegado', 403
        
  if 'contenido' in data:
    contenido = data['contenido']
  else:
    contenido = ''

  if 'categoria' in data:
    nombre_categoria = data['categoria']
  else:
    nombre_categoria = 'Diario personal'
  
  if 'fecha_actual' in data:
    fecha_actual = data['fecha_actual']
  else:
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  
  if 'titulo' in data:
    titulo = data['titulo']

    entrada.update(entrada_id, titulo, fecha_actual, contenido, nombre_categoria)
    return 'Entrada actualizada', 200
  else:
    return 'Título requerido', 422

@diario_blueprint.route('/diario/delete', methods=['DELETE'])
def entrada_delete():
  data = request.get_json()

  usuario_id = get_userid(data['token'])
  entrada_id = data['entrada_id']

  tabla_entrada = entrada.get(entrada_id)
  if len(tabla_entrada) > 0:
    if tabla_entrada[0][1] == usuario_id:
        entrada.delete(entrada_id)
        return 'Actividad borrada', 200
    
  return 'Acceso denegado', 403



def get_userid(token):
  try:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), None)
    userid = idinfo['sub']
  except ValueError:
    return False
  return userid