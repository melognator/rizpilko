from .. import db_connection

# actividad crud

# tabla_actividad = '''
# CREATE TABLE Actividad(
# ID INTEGER NOT NULL,
# usuario INTEGER NOT NULL,
# categoria INTEGER,
# titulo TEXT NOT NULL,
# fecha_comienzo TEXT NOT NULL,
# fecha_fin TEXT NOT NULL,
# PRIMARY KEY (ID),
# FOREIGN KEY (usuario) REFERENCES Usuario(ID)
# );
# '''

def create(usuario, categoria, titulo, fecha_comienzo, fecha_fin):
  sql = f"""
        INSERT INTO Actividad(usuario, categoria, titulo, fecha_comienzo, fecha_fin)
        VALUES ('{usuario}', '{categoria}' ,'{titulo}', '{fecha_comienzo}', '{fecha_fin}')
    """
  db_connection.ejecutar_sql(sql)


def delete(id):
  sql = f"""
        DELETE FROM Actividad WHERE ID = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def update(id, categoria, titulo, fecha_comienzo, fecha_fin):
  sql = f"""
        UPDATE Actividad 
        SET categoria = '{categoria}',
        titulo = '{titulo}',
        fecha_comienzo = '{fecha_comienzo}',
        fecha_fin = '{fecha_fin}'
        WHERE ID = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def cambiar_titulo(id, nuevo_titulo):
  sql = f"""
        UPDATE Actividad
        SET titulo = '{nuevo_titulo}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def cambiar_categoria(id, nueva_categoria):
  sql = f"""
        UPDATE Actividad
        SET categoria = '{nueva_categoria}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def cambiar_fechas(id, nueva_fecha_comienzo, nueva_fecha_fin):
  sql = f"""
        UPDATE Actividad
        SET fecha_comienzo = '{nueva_fecha_comienzo}',
        fecha_fin = '{nueva_fecha_fin}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def get(id):
  sql = f"""
        SELECT Actividad.ID, Actividad.usuario, Categoria.nombre, Actividad.titulo, Actividad.fecha_comienzo, Actividad.fecha_fin FROM Actividad, Categoria WHERE Actividad.id = '{id}' AND Actividad.categoria = Categoria.id;
    """
  data = db_connection.ejecutar_sql(sql)
  return data

  # <p>ID: {actividad[0]}</p>
  #   <p>Usuario: {actividad[1]}</p>
  #   <p>Categoría: {actividad[2]}</p>
  #   <p>Título: {actividad[3]}</p>
  #   <p>Fecha comienzo: {actividad[4]}</p>
  #   <p>Fecha fin: {actividad[5]}</p>

def getall(usuario):
  sql = f"""
        SELECT * FROM Actividad WHERE usuario = '{usuario}' ORDER BY ID DESC;
    """
  data = db_connection.ejecutar_sql(sql)
  return data
