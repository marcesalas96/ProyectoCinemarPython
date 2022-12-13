import sqlite3
from datetime import datetime
from Class.clase_descuento import Descuento
class Reserva:
    def __init__(self,tupla, idUsuario):
        self.__tupla = tupla
        self.__idUsuario = idUsuario
    
    def crearReserva(self):  
        db = sqlite3.connect("cinemar.sqlite3")
        conexion = db.cursor()
        d = datetime.now()
        userData = conexion.execute(f"SELECT tiene_tarjeta from usuario where id_usuario = {self.__idUsuario}")
        idUsuario = userData.fetchone()
        dia = d.weekday()
        descuento = Descuento(self.__tupla[5], idUsuario[0],dia)
        valorEntrada = descuento.porcentajeDescuento()
        horaActual = datetime.now().time()
        fechaActual = datetime.now().date()
        conexion.execute(f"INSERT INTO reserva (id_funcion, horario, fecha, titulo, duracion, tipo, valorEntrada, fechaDeCreacion, horaDeCreacion, id_usuario) VALUES ({self.__tupla[0]},'{self.__tupla[1]}','{self.__tupla[2]}','{self.__tupla[3]}','{self.__tupla[4]}','{self.__tupla[5]}','{valorEntrada}', '{fechaActual}', '{horaActual}', {self.__idUsuario} )")
        db.commit()
        db.close()