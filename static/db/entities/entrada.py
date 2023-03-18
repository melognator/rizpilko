from .. import db_connection

#  entrada crud

# tabla_entrada = '''
# CREATE TABLE Entrada(
# ID INTEGER NOT NULL,
# usuario INTEGER NOT NULL,
# titulo TEXT NOT NULL,
# fecha_modificacion TEXT NOT NULL,
# contenido TEXT,
# categoria TEXT,
# PRIMARY KEY (ID),
# FOREIGN KEY (usuario) REFERENCES Usuario(ID)
# );
# '''


def create(usuario, titulo, fecha_modificacion, contenido, categoria):
  sql = f"""
        INSERT INTO Entrada(usuario, titulo, fecha_modificacion, contenido, categoria)
        VALUES ('{usuario}','{titulo}', '{fecha_modificacion}', '{contenido}', '{categoria}')
    """
  db_connection.ejecutar_sql(sql)
  sql = f"""
      SELECT MAX(ID) FROM Entrada WHERE usuario = '{usuario}';
  """ 
  data = db_connection.ejecutar_sql(sql)
  return data



def delete(id):
  sql = f"""
        DELETE FROM Entrada WHERE ID = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def update(id, nuevo_titulo, nueva_fecha, nuevo_contenido, nueva_categoria):
  sql = f"""
        UPDATE Entrada
        SET titulo = '{nuevo_titulo}',
        fecha_modificacion = '{nueva_fecha}',
        contenido = '{nuevo_contenido}',
        categoria = '{nueva_categoria}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def cambiar_titulo(id, nuevo_titulo):
  sql = f"""
        UPDATE Entrada
        SET titulo = '{nuevo_titulo}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def cambiar_contenido(id, nuevo_contenido, nueva_fecha):
  sql = f"""
        UPDATE Entrada
        SET contenido = '{nuevo_contenido}',
        fecha_modificacion = '{nueva_fecha}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def cambiar_categoria(id, nueva_categoria):
  sql = f"""
        UPDATE Entrada
        SET categoria = '{nueva_categoria}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def get(id):
  sql = f"""
        SELECT * FROM Entrada WHERE id = '{id}';
    """
  data = db_connection.ejecutar_sql(sql)
  return data

def getall(usuario):
  sql = f"""
        SELECT * FROM Entrada WHERE usuario = '{usuario}';
    """
  data = db_connection.ejecutar_sql(sql)
  return data