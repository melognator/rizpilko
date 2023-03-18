import sqlite3
from .. import classes

# connection
url = '/home/runner/Rizpi/static/db/database.db'

def ejecutar_multiple_sql(sql):
  try:
      conexion = sqlite3.connect(url)
  except Exception as e:
      print(e)
  cur = conexion.cursor()
  cur.executescript(sql)

  conexion.commit()
  conexion.close()

def ejecutar_sql(sql):
  try:
      conexion = sqlite3.connect(url)
  except Exception as e:
      print(e)
  cur = conexion.cursor()
  cur.execute(sql)

  filas = cur.fetchall()

  conexion.commit()
  conexion.close()

  return filas

