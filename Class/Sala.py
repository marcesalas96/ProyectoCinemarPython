import sqlite3
from Class.Funcion import Funcion
class Sala :
    def __init__(self, id, cantidadDeButacas ):
        self.__id = id
        self.__cantidadButacas = cantidadDeButacas
    def getId(self):
        return self.__id
    def getCantidadButacas(self):
        return self.__butacas
    def mostrarDatos(self):
        cadena= "\nNumero de sala: "+ str(self.__id)
        return cadena
        
    
    def crearSalaBDD(self):
        db = sqlite3.connect("cinemar.sqlite3")
        conexion = db.cursor()
        conexion.execute(f"INSERT INTO sala (id_sala, cantidad_butacas) VALUES ({self.__id}, {self.__cantidadButacas})")
        db.commit()
        db.close()