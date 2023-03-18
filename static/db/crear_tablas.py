import sqlite3

tabla_usuario = '''
CREATE TABLE Usuario(
ID TEXT NOT NULL,
nombre TEXT,
experiencia INTEGER DEFAULT 0,
PRIMARY KEY (ID)
);
'''

tabla_categoria = '''
CREATE TABLE Categoria(
ID INTEGER NOT NULL,
usuario TEXT NOT NULL,
nombre TEXT NOT NULL,
PRIMARY KEY (ID),
FOREIGN KEY (usuario) REFERENCES Usuario(ID)
);
'''

tabla_tarea = '''
CREATE TABLE Tarea(
ID INTEGER NOT NULL,
usuario TEXT NOT NULL,
categoria INTEGER DEFAULT 0,
titulo TEXT NOT NULL,
descripcion TEXT,
prioridad INTEGER DEFAULT 0,
completada INTEGER DEFAULT 0,
PRIMARY KEY (ID),
FOREIGN KEY (usuario) REFERENCES Usuario(ID),
FOREIGN KEY (categoria) REFERENCES Categoria(ID)
);
'''

tabla_tarea_recurrente = '''
CREATE TABLE Tarea_recurrente(
ID INTEGER NOT NULL,
frecuencia TEXT,
fecha_comienzo TEXT,
PRIMARY KEY (ID),
FOREIGN KEY (ID) REFERENCES Tarea(ID)
);
'''

tabla_tarea_no_recurrente = '''
CREATE TABLE Tarea_no_recurrente(
ID INTEGER NOT NULL,
fecha_limite TEXT,
fecha_recordatorio TEXT,
PRIMARY KEY (ID),
FOREIGN KEY (ID) REFERENCES Tarea(ID)
);
'''

tabla_entrada = '''
CREATE TABLE Entrada(
ID INTEGER NOT NULL,
usuario TEXT NOT NULL,
titulo TEXT NOT NULL,
fecha_modificacion TEXT NOT NULL,
contenido TEXT,
categoria TEXT,
PRIMARY KEY (ID),
FOREIGN KEY (usuario) REFERENCES Usuario(ID)
);
'''

tabla_actividad = '''
CREATE TABLE Actividad(
ID INTEGER NOT NULL,
usuario TEXT NOT NULL,
categoria INTEGER DEFAULT 0,
titulo TEXT NOT NULL,
fecha_comienzo TEXT NOT NULL,
fecha_fin TEXT NOT NULL,
PRIMARY KEY (ID),
FOREIGN KEY (usuario) REFERENCES Usuario(ID),
FOREIGN KEY (categoria) REFERENCES Categoria(ID)
);
'''

tabla_consejo = '''
CREATE TABLE Consejo(
ID INTEGER NOT NULL,
consejo TEXT,
PRIMARY KEY (ID)
);
'''

# try:
#     print('Creando Base de datos..')
#     conexion = sqlite3.connect('/static/db/database.db')

#     print('Creando Tablas..')
#     conexion.execute(tabla_actividad)
#     conexion.execute(tabla_categoria)
#     conexion.execute(tabla_consejo)
#     conexion.execute(tabla_entrada)
#     conexion.execute(tabla_tarea)
#     conexion.execute(tabla_tarea_no_recurrente)
#     conexion.execute(tabla_tarea_recurrente)
#     conexion.execute(tabla_usuario)
    

#     conexion.close()
#     print('Creacion Finalizada.')
# except Exception as e:
#     print(f'Error creando base de datos: {e}', e)


print('Creando Base de datos..')
conexion = sqlite3.connect('/home/runner/Rizpi/static/db/database.db')

print('Creando Tablas..')
conexion.execute(tabla_actividad)
conexion.execute(tabla_categoria)
conexion.execute(tabla_consejo)
conexion.execute(tabla_entrada)
conexion.execute(tabla_tarea)
conexion.execute(tabla_tarea_no_recurrente)
conexion.execute(tabla_tarea_recurrente)
conexion.execute(tabla_usuario)

categoria_0 = f"""
      INSERT INTO Usuario(id)
      VALUES (0);
      INSERT INTO Categoria(id, usuario, nombre)
      VALUES (0, 0, 'None');
  """

conexion.executescript(categoria_0)



conexion.close()
print('Creacion Finalizada.')