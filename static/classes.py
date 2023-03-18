import random

def generar_codigo_recuperacion():
  codigo = ""
  for x in range(9):
    codigo += str(random.randint(0,9))


class Usuario:
  def __init__(self, id, login, password, codigo_recuperacion, nombre, experiencia, categorias, tareas, entradas, actividades):
    self.id = id
    self.login = login
    self.password = password
    self.codigo_recuperacion = codigo_recuperacion
    self.nombre = nombre
    self.experiencia = experiencia
    self.categorias = categorias
    self.tareas = tareas
    self.entradas = entradas
    self.actividades = actividades

class Tarea:
  def __init__(self, categoria, titulo, descripcion, prioridad, terminada):
    self.categoria = categoria
    self.titulo = titulo
    self.descripcion = descripcion
    self.prioridad = prioridad
    self.terminada = terminada

class TareaRecurrente(Tarea):
  def __init__(self, categoria, titulo, descripcion, prioridad, terminada, frecuencia, fecha_comienzo):
    super.__init__(self, categoria, titulo, descripcion, prioridad, terminada)
    self.frecuencia = frecuencia
    self.fecha_comienzo = fecha_comienzo

class TareaNoRecurrente(Tarea):
  def __init__(self, categoria, titulo, descripcion, prioridad, terminada, fecha_limite, fecha_recordatorio):
    super.__init__(self, categoria, titulo, descripcion, prioridad, terminada)
    self.fecha_limite = fecha_limite
    self.fecha_recordatorio = fecha_recordatorio

class Entrada:
  def __init__(self, titulo, fecha_modificacion, contenido, categoria):
    self.titulo = titulo
    self.fecha_modificacion = fecha_modificacion
    self.contenido = contenido
    self.categoria = categoria

class Actividad:
  def __init__(self, categoria, titulo, fecha_comienzo, fecha_fin):
    self.categoria = categoria
    self.titulo = titulo
    self.fecha_comienzo = fecha_comienzo
    self.fecha_fin = fecha_fin