import sqlite3 as sqlite3
class Butaca:
    def __init__(self, idFuncion, posicion):
        self.__idFuncion = idFuncion
        self.__posiscion = posicion
        self.__ocupado = False
    @property
    def getIdFuncion(self):
        return self.__idFuncion
    @property
    def getPosicion(self):
        return self.__posiscion
    @property
    def getOcupado(self):
        return self.__ocupado
    
    def actualizarOcupado(self):
        self.__ocupado = not self.__ocupado
        return "ocupado= "+ str(self.__ocupado)
        
    def guardarButacaBDD(self):
        bd = sqlite3.connect("cinemar.sqlite3")
        conexion = bd.cursor()
        conexion.execute(f"INSERT INTO butaca (pos, ocupado, id_funcion) VALUES ({self.__posiscion}, {self.__ocupado}, {self.__idFuncion}")
        bd.commit()
        bd.close()