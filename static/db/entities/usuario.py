from .. import db_connection

# usuario crud

def create(id, nombre):
  id = int(id)
  sql = f"""
        INSERT INTO Usuario(id, nombre)
        VALUES ('{id}','{nombre}')
    """
  db_connection.ejecutar_sql(sql)


def delete(id):
  sql = f"""
        DELETE FROM Usuario WHERE ID = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def cambiar_nombre(id, nuevo_nombre):
  sql = f"""
        UPDATE Usuario
        SET nombre = '{nuevo_nombre}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def incrementar_exp(id, cantidad_exp):
  sql = f"""
        UPDATE Usuario
        SET experiencia = experiencia + {cantidad_exp}
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)
  
def get(id):
  sql = f"""
        SELECT * FROM Usuario WHERE id = '{id}';
    """
  data = db_connection.ejecutar_sql(sql)
  return data

def getall():
  sql = f"""
        SELECT * FROM Usuario;
    """
  data = db_connection.ejecutar_sql(sql)
  return data