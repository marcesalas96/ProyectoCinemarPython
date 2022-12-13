from Class.Cliente import Cliente
from Class.Usuario import Usuario
from Class.clase_descuento import Descuento
from datetime import datetime
# cliente = Cliente("Carla", "Allende", "carAll@gmail.com", 18, "carall", "carall")
# cliente.setAdmin()
# cliente.registroUsuario()
usuario = Usuario("carall", "carall")
usuario.login()

# import sqlite3

# db = sqlite3.connect("cinemar.sqlite3")
# conexion = db.cursor()
# data = conexion.execute("SELECT funcion.id_funcion, funcion.horario, funcion.fecha, pelicula.titulo, pelicula.duracion, pelicula.tipo FROM sala INNER JOIN pelicula ON pelicula.id_sala = sala.id_sala INNER JOIN funcion ON funcion.id_sala = sala.id_sala ")
# tupla = data.fetchall()
# for peli in tupla:
#     print(peli)
#     print("\n")

# d = datetime.now()
# dia = d.weekday()
# descuento = Descuento("2D", False, str(dia))
# descuento.porcentajeDescuento()