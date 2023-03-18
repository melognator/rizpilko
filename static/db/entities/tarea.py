from .. import db_connection



# tarea crud

# usuario INTEGER NOT NULL,
# categoria INTEGER,
# titulo TEXT NOT NULL,
# descripcion TEXT,
# prioridad INTEGER DEFAULT 0,

# recurrente
# frecuencia TEXT,
# fecha_comienzo TEXT,

# no recurrente
# fecha_limite TEXT,
# fecha_recordatiorio TEXT,

def recurrente_create(usuario, categoria, titulo, descripcion, prioridad, frecuencia, fecha_comienzo):
  sql = f"""
        INSERT INTO Tarea(usuario, categoria, titulo, descripcion, prioridad)
        VALUES ('{usuario}', '{categoria}', '{titulo}', '{descripcion}', '{prioridad}');
        INSERT INTO Tarea_recurrente(ID, frecuencia, fecha_comienzo)
        VALUES (last_insert_rowid(), '{frecuencia}', '{fecha_comienzo}');
    """
  db_connection.ejecutar_multiple_sql(sql)
  sql = f"""
      SELECT MAX(ID) FROM Tarea WHERE usuario = '{usuario}';
  """ 
  data = db_connection.ejecutar_sql(sql)
  return data

def no_recurrente_create(usuario, categoria, titulo, descripcion, prioridad, fecha_limite, fecha_recordatorio):
  sql = f"""
        INSERT INTO Tarea(usuario, categoria, titulo, descripcion, prioridad)
        VALUES ('{usuario}', '{categoria}', '{titulo}', '{descripcion}', '{prioridad}');
        INSERT INTO Tarea_no_recurrente(ID, fecha_limite, fecha_recordatorio)
        VALUES (last_insert_rowid(), '{fecha_limite}', '{fecha_recordatorio}');
    """
  db_connection.ejecutar_multiple_sql(sql)
  sql = f"""
        SELECT MAX(ID) FROM Tarea WHERE usuario = '{usuario}';
    """ 
  data = db_connection.ejecutar_sql(sql)
  return data

def recurrente_delete(id):
  sql = f"""
        DELETE FROM Tarea_recurrente WHERE ID = '{id}';
        DELETE FROM Tarea WHERE ID = '{id}';
    """
  db_connection.ejecutar_multiple_sql(sql)

def no_recurrente_delete(id):
  sql = f"""
        DELETE FROM Tarea_no_recurrente WHERE ID = '{id}';
        DELETE FROM Tarea WHERE ID = '{id}';
    """
  db_connection.ejecutar_multiple_sql(sql)

def completar(id):
  sql = f"""
        UPDATE Tarea 
        SET completada = 1
        WHERE ID = '{id}';
    """
  db_connection.ejecutar_sql(sql)

def descompletar(id):
  sql = f"""
        UPDATE Tarea 
        SET completada = 0
        WHERE ID = '{id}';
    """
  db_connection.ejecutar_sql(sql)

# categoria INTEGER DEFAULT 0,
# titulo TEXT NOT NULL,
# descripcion TEXT,
# prioridad INTEGER DEFAULT 0,

# recurrente
# frecuencia TEXT,
# fecha_comienzo TEXT,

# no recurrente
# fecha_limite TEXT,
# fecha_recordatorio TEXT,

def recurrente_update(id, categoria, titulo, descripcion, prioridad, frecuencia, fecha_comienzo):
  sql = f"""
        UPDATE Tarea
        SET categoria = '{categoria}',
        titulo = '{titulo}',
        descripcion = '{descripcion}',
        prioridad = '{prioridad}'
        WHERE ID = '{id}';

        UPDATE Tarea_recurrente
        SET frecuencia = '{frecuencia}',
        fecha_comienzo = '{fecha_comienzo}'
        WHERE ID = '{id}';
    """
  db_connection.ejecutar_multiple_sql(sql)

def no_recurrente_update(id, categoria, titulo, descripcion, prioridad, fecha_limite, fecha_recordatorio):
  sql = f"""
        UPDATE Tarea
        SET categoria = '{categoria}',
        titulo = '{titulo}',
        descripcion = '{descripcion}',
        prioridad = '{prioridad}'
        WHERE ID = '{id}';

        UPDATE Tarea_no_recurrente
        SET fecha_limite = '{fecha_limite}',
        fecha_recordatorio = '{fecha_recordatorio}'
        WHERE ID = '{id}';
    """
  db_connection.ejecutar_multiple_sql(sql)

def recurrente_get(id):
  sql = f"""
        SELECT Tarea.*, Tarea_recurrente.frecuencia, Tarea_recurrente.fecha_comienzo FROM Tarea, Tarea_recurrente WHERE Tarea.ID = '{id}' AND Tarea_recurrente.ID = '{id}';
    """
  data = db_connection.ejecutar_sql(sql)
  return data

def no_recurrente_get(id):
  sql = f"""
        SELECT Tarea.*, Tarea_no_recurrente.fecha_limite, Tarea_no_recurrente.fecha_recordatorio FROM Tarea, Tarea_no_recurrente WHERE Tarea.ID = '{id}' AND Tarea_no_recurrente.ID = '{id}';
    """ 
  data = db_connection.ejecutar_sql(sql)
  return data

def recurrente_getall(usuario):
  sql = f"""
        SELECT Tarea.*, Tarea_recurrente.frecuencia, Tarea_recurrente.fecha_comienzo FROM Tarea, Tarea_recurrente WHERE Tarea.usuario = '{usuario}' AND Tarea.ID = Tarea_recurrente.ID;
    """
  data = db_connection.ejecutar_sql(sql)
  return data

def no_recurrente_getall(usuario):
  sql = f"""
        SELECT Tarea.*, Tarea_no_recurrente.fecha_limite, Tarea_no_recurrente.fecha_recordatorio FROM Tarea, Tarea_no_recurrente WHERE Tarea.usuario = '{usuario}' AND Tarea.ID = Tarea_no_recurrente.ID;
    """ 
  data = db_connection.ejecutar_sql(sql)
  return data