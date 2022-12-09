import sqlite3

class Funcion:
  def __init__(self, id_funcion, horario, fecha, id_sala):
    self.__id_funcion= id_funcion
    self.__horario= horario
    self.__fecha= fecha
    self.__idsala = id_sala
    
  def getId_Funcion(self):
    return self.__id_funcion
  def getHorario(self):
    return self.__horario
  def setFecha(self):
    return self.__fecha
  def getId_Sala(self):
    return self.__id_sala
  def mostrarFuncion(self):
    print("\nId_Funcion: "+self.getid_funcion()  +"\nId_Sala: "+self.getid_sala)
  
  def guardarFuncionBDD(self):
    db = sqlite3.connect("cinemar.sqlite3")
    conexion = db.cursor()
    conexion.execute(f"INSERT INTO funcion (id_funcion, horario, fecha, id_sala) VALUES ({self.__id_funcion}, '{self.__horario}', {self.__fecha}, {self.__idsala})")
    db.commit()
    db.close()
    
funcion = Funcion(1,"17:00:00", "2022-12-05", 1)
funcion.guardarFuncionBDD()