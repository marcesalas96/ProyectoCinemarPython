import sqlite3

class Sala :
    def __init__(self, id, cantidadDeButacas ):
        self.__id = id
        self.__butacas = cantidadDeButacas
        
    def getId(self):
        print("ENTRE FUNCION")
        return self.__id
    
    def mostrarDatos(self):
        cadena= "\nNumero de sala: "+ str(self.__id)
        return cadena
        
    
    def crearSalaBDD(self):
        db = sqlite3.connect("cinemar.sqlite3")
        conexion = db.cursor()
        conexion.execute(f"INSERT INTO sala (id_sala, cantidad_butacas) VALUES ({self.__id}, {self.__butacas})")
        db.commit()
        db.close()