import sqlite3

class Reserva:
    def __init__(self,tupla, idUsuario):
        self.__tupla = tupla
        self.__idUsuario = idUsuario
        self.__lista = []
    
    def crearReserva(self):
        for item in self.__tupla:
            self.__lista.append(item)
        db = sqlite3.connect("cinemar.sqlite3")
        conexion = db.cursor()
        conexion.execute(f"INSERT INTO reserva (datos_reserva, id_usuario) VALUES ({self.__lista}, {self.__idUsuario})")
        db.commit()
        db.close()