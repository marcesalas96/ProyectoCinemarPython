import sqlite3

conexion = sqlite3.connect("cinemar.sqlite3")
cursor = conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuario (
                id_usuario integer primary key autoincrement, nombre_usuario TEXT NOT NULL, 
                contraseña TEXT NOT NULL,
                correo text not null,
                admin BOOLEAN,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                edad INTEGER NOT NULL,
                tiene_tarjeta boolean not null)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS sala(
                id_sala integer primary key ,
                cantidad_butacas integer not null)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS pelicula(
                id_pelicula integer PRIMARY KEY ,
                titulo text,
                duracion int,
                idioma text,
                edad integer,
                descripcion text,
                genero text,
                tipo text not null,
                id_sala integer,
                FOREIGN KEY(id_sala) REFERENCES sala(id_sala))""")

cursor.execute("""CREATE TABLE IF NOT EXISTS funcion (
                id_funcion integer PRIMARY KEY,
                horario time,
                fecha date,
                id_sala integer,
                FOREIGN KEY(id_sala) REFERENCES sala(id_sala))""")

cursor.execute("""CREATE TABLE IF NOT EXISTS butaca(
                pos integer primary key,
                ocupado boolean,
                id_funcion integer,
                FOREIGN KEY(id_funcion) REFERENCES funcion(id_funcion))
                """)
conexion.commit()
conexion.close()