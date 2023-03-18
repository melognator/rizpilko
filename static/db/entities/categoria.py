from .. import db_connection

# categoria crud

def create(usuario, nombre):
  sql = f"""
        INSERT INTO Categoria(usuario, nombre)
        VALUES ('{usuario}','{nombre}')
    """
  db_connection.ejecutar_sql(sql)

def delete(id):
  sql = f"""
        DELETE FROM Categoria WHERE ID = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def update(id, nuevo_nombre):
  sql = f"""
        UPDATE Categoria
        SET nombre = '{nuevo_nombre}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def get(id):
  sql = f"""
        SELECT * FROM Categoria WHERE id = '{id}';
    """
  data = db_connection.ejecutar_sql(sql)
  return data

def getall(usuario):
  sql = f"""
        SELECT * FROM Categoria WHERE usuario = '{usuario}';
    """
  data = db_connection.ejecutar_sql(sql)
  return data