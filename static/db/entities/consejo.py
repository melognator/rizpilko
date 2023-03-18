from .. import db_connection


# crud consejos

# tabla_consejo = '''
# CREATE TABLE Consejo(
# ID INTEGER NOT NULL,
# consejo TEXT,
# PRIMARY KEY (ID)
# );
# '''

def create(consejo):
  sql = f"""
        INSERT INTO Consejo(consejo)
        VALUES ('{consejo}')
    """
  db_connection.ejecutar_sql(sql)


def delete(id):
  sql = f"""
        DELETE FROM Consejo WHERE ID = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def cambiar_contenido(id, nuevo_contenido):
  sql = f"""
        UPDATE Consejo
        SET consejo = '{nuevo_contenido}'
        WHERE id = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def get(id):
  sql = f"""
        SELECT * FROM Consejo WHERE id = '{id}';
    """
  data = db_connection.ejecutar_sql(sql)
  return data

def getall():
  sql = f"""
        SELECT * FROM Consejo;
    """
  data = db_connection.ejecutar_sql(sql)
  return data