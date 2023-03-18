from flask import Blueprint, request, jsonify, render_template
from google.oauth2 import id_token
from google.auth.transport import requests
from ..db.entities import tarea, categoria

tarea_blueprint = Blueprint('tarea', __name__,template_folder='')


# tareas

@tarea_blueprint.route('/tareas', methods=['POST'])
def tarea_no_recurrente_getall():
  data = request.get_json()
  
  usuario_id = get_userid(data['token'])
  tareas = tarea.no_recurrente_getall(usuario_id)
  categorias = categoria.getall(usuario_id)
  return render_template('tareas.html', tareas=tareas, categorias=categorias)

@tarea_blueprint.route('/tareas/completar', methods=['POST'])
def completar_tarea():
  data = request.get_json()
  tarea_id = data['tarea_id']
  usuario_id = get_userid(data['token'])
  tabla_tarea_recurrente = tarea.recurrente_get(tarea_id)
  tabla_tarea_no_recurrente = tarea.no_recurrente_get(tarea_id)
  if len(tabla_tarea_recurrente) > 0:
    if tabla_tarea_recurrente[0][1] == usuario_id:
      tarea.completar(tarea_id)
      return 'Listo', 200
  if len(tabla_tarea_no_recurrente) > 0:
    if tabla_tarea_no_recurrente[0][1] == usuario_id:
      tarea.completar(tarea_id)
      return 'Listo', 200
    
  return 'Acceso denegado', 403

@tarea_blueprint.route('/tareas/descompletar', methods=['POST'])
def descompletar_tarea():
  data = request.get_json()
  tarea_id = data['tarea_id']
  usuario_id = get_userid(data['token'])
  tabla_tarea_recurrente = tarea.recurrente_get(tarea_id)
  tabla_tarea_no_recurrente = tarea.no_recurrente_get(tarea_id)
  if len(tabla_tarea_recurrente) > 0:
    if tabla_tarea_recurrente[0][1] == usuario_id:
      tarea.descompletar(tarea_id)
      return 'Listo', 200
  if len(tabla_tarea_no_recurrente) > 0:
    if tabla_tarea_no_recurrente[0][1] == usuario_id:
      tarea.descompletar(tarea_id)
      return 'Listo', 200
    
  return 'Acceso denegado', 403


@tarea_blueprint.route('/calendario', methods=['POST'])
def tarea_recurrente_getall():
  data = request.get_json()
  
  usuario_id = get_userid(data['token'])
  tareas = tarea.recurrente_getall(usuario_id)
  categorias = categoria.getall(usuario_id)
  return render_template('calendario.html', tareas=tareas, categorias=categorias)

# @tarea_blueprint.route('/load', methods=['POST'])
# def load_everything():
#     data = request.get_json()
#     usuario_id = get_userid(data['token'])
#     tareas = render_template('tareas.html', tareas=tarea.no_recurrente_getall(usuario_id))
#     calendario = render_template('calendario.html', calendario=tarea.recurrente_getall(usuario_id))
    
#     return '{} {}'.format(tareas, calendario), 200



@tarea_blueprint.route('/calendario/create', methods=['POST'])
def tarea_recurrente_create():
  data = request.get_json()

  usuario_id = get_userid(data['token'])

  if 'categoria' in data:
    categoria_id = data['categoria']
  else:
    categoria_id = 0

  if 'descripcion' in data:
    descripcion = data['descripcion']
  else:
    descripcion = ''

  if 'prioridad' in data:
    prioridad = data['prioridad']
  else:
    prioridad = 0
  
  if 'frecuencia' in data:
    frecuencia = data['frecuencia']
  else:
    frecuencia = ""

  if 'fecha_comienzo' in data:
    fecha_comienzo = data['fecha_comienzo']
  else:
    fecha_comienzo = ""

  if 'titulo' in data:
    titulo = data['titulo']

    id_tarea = tarea.recurrente_create(usuario_id, categoria_id, titulo, descripcion, prioridad, frecuencia, fecha_comienzo)
    return jsonify(id_tarea[0][0]), 200
  else:
    return 'Título requerido', 422

@tarea_blueprint.route('/tareas/create', methods=['POST'])
def tarea_no_recurrente_create():
  data = request.get_json()

  usuario_id = get_userid(data['token'])

  if 'categoria' in data:
    categoria_id = data['categoria']
  else:
    categoria_id = 0

  if 'descripcion' in data:
    descripcion = data['descripcion']
  else:
    descripcion = ''

  if 'prioridad' in data:
    prioridad = data['prioridad']
  else:
    prioridad = 0
  
  if 'fecha_limite' in data:
    fecha_limite = data['fecha_limite']
  else:
    fecha_limite = ""

  if 'fecha_recordatorio' in data:
    fecha_recordatorio = data['fecha_recordatorio']
  else:
    fecha_recordatorio = ""

  if 'titulo' in data:
    titulo = data['titulo']
    id_tarea = tarea.no_recurrente_create(usuario_id, categoria_id, titulo, descripcion, prioridad,fecha_limite, fecha_recordatorio)

    return jsonify(id_tarea[0][0]), 200
  else:
    return 'Título requerido', 422


@tarea_blueprint.route('/usuario/<int:usuario_id>/tarea_recurrente/<int:tarea_id>', methods=['GET'])
def tarea_recurrente_get(usuario_id, tarea_id):
  fila_tarea = tarea.recurrente_get(tarea_id)[0]
  html = f"""
    <p>ID: {fila_tarea[0]}</p>
    <p>Usuario: {fila_tarea[1]}</p>
    <p>Categoría: {fila_tarea[2]}</p>
    <p>Título: {fila_tarea[3]}</p>
    <p>Descripción: {fila_tarea[4]}</p>
    <p>Prioridad: {fila_tarea[5]}</p>
    <p>Completada: {fila_tarea[6]}</p>
    <p>Frecuencia: {fila_tarea[7]}</p>
    <p>Fecha comienzo: {fila_tarea[8]}</p>
    <hr>
    """
  return html, 200

@tarea_blueprint.route('/usuario/<int:usuario_id>/tarea_no_recurrente/<int:tarea_id>', methods=['GET'])
def tarea_no_recurrente_get(usuario_id, tarea_id):
  fila_tarea = tarea.no_recurrente_get(tarea_id)[0]
  html = f"""
    <p>ID: {fila_tarea[0]}</p>
    <p>Usuario: {fila_tarea[1]}</p>
    <p>Categoría: {fila_tarea[2]}</p>
    <p>Título: {fila_tarea[3]}</p>
    <p>Descripción: {fila_tarea[4]}</p>
    <p>Prioridad: {fila_tarea[5]}</p>
    <p>Completada: {fila_tarea[6]}</p>
    <p>Fecha límite: {fila_tarea[7]}</p>
    <p>Fecha recordatorio: {fila_tarea[8]}</p>
    <hr>
    """
  return html, 200


@tarea_blueprint.route('/tareas/delete', methods=['DELETE'])
def tarea_delete():
  data = request.get_json()

  usuario_id = get_userid(data['token'])
  tarea_id = data['tarea_id']

  tabla_tarea_recurrente = tarea.recurrente_get(tarea_id)
  tabla_tarea_no_recurrente = tarea.no_recurrente_get(tarea_id)
  if len(tabla_tarea_recurrente) > 0:
    if tabla_tarea_recurrente[0][1] == usuario_id:
      tarea.recurrente_delete(tarea_id)
      return "Tarea eliminada", 200
  if len(tabla_tarea_no_recurrente) > 0:
    if tabla_tarea_no_recurrente[0][1] == usuario_id:
      tarea.no_recurrente_delete(tarea_id)
      return "Tarea eliminada", 200
    
  return 'Acceso denegado', 403


@tarea_blueprint.route('/calendario', methods=['PUT'])
def tarea_recurrente_update():
  data = request.get_json()

  usuario_id = get_userid(data['token'])
  tarea_id = data['tarea_id']

  tabla_tarea_recurrente = tarea.recurrente_get(tarea_id)

  if len(tabla_tarea_recurrente) == 0:
    return 'Acceso denegado', 403

  if len(tabla_tarea_recurrente) > 0:
    if tabla_tarea_recurrente[0][1] != usuario_id:
      return 'Acceso denegado', 403
  if 'categoria' in data:
    categoria_id = data['categoria']
  else:
    categoria_id = 0

  if 'descripcion' in data:
    descripcion = data['descripcion']
  else:
    descripcion = ''

  if 'prioridad' in data:
    prioridad = data['prioridad']
  else:
    prioridad = 0
  
  if 'frecuencia' in data:
    frecuencia = data['frecuencia']
  else:
    frecuencia = ""

  if 'fecha_comienzo' in data:
    fecha_comienzo = data['fecha_comienzo']
  else:
    fecha_comienzo = ""

  if 'titulo' in data:
    titulo = data['titulo']
  else:
    titulo = ''

  tarea.recurrente_update(tarea_id, categoria_id, titulo, descripcion, prioridad, frecuencia, fecha_comienzo)
  return 'Tarea recurrente actualizada', 200


@tarea_blueprint.route('/tareas', methods=['PUT'])
def tarea_no_recurrente_update():
  data = request.get_json()

  usuario_id = get_userid(data['token'])
  tarea_id = data['tarea_id']

  tabla_tarea_no_recurrente = tarea.no_recurrente_get(tarea_id)

  if len(tabla_tarea_no_recurrente) == 0:
    return 'Acceso denegado', 403

  if len(tabla_tarea_no_recurrente) > 0:
    if tabla_tarea_no_recurrente[0][1] != usuario_id:
      return 'Acceso denegado', 403

  if 'categoria' in data:
    categoria_id = data['categoria']
  else:
    categoria_id = 0

  if 'descripcion' in data:
    descripcion = data['descripcion']
  else:
    descripcion = ''

  if 'prioridad' in data:
    prioridad = data['prioridad']
  else:
    prioridad = 0
  
  if 'fecha_limite' in data:
    fecha_limite = data['fecha_limite']
  else:
    fecha_limite = ""

  if 'fecha_recordatorio' in data:
    fecha_recordatorio = data['fecha_recordatorio']
  else:
    fecha_recordatorio = ""

  if 'titulo' in data:
    titulo = data['titulo']
  else:
    titulo = ''

  tarea.no_recurrente_update(tarea_id, categoria_id, titulo, descripcion, prioridad, fecha_limite, fecha_recordatorio)
  return 'Tarea no recurrente actualizada', 200


def get_userid(token):
  try:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), None)
    userid = idinfo['sub']
  except ValueError:
    return False
  return userid