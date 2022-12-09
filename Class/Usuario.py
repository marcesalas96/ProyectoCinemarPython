import sqlite3
class Usuario:

  def __init__(self, nombre_usuario, clave):
    self.__nombre_usuario = nombre_usuario
    self.__clave = clave
    
  def __str__(self):
    cadena= "\nNombre_Usuario: "+self.__nombre_usuario
    cadena+= "\nClave: "+str(self.__clave)
    cadena+= "\nTipo: "+str(self.__tipo)
    return cadena

  @property 
  def get_nombreUsuario(self):
    return self.__nombre_usuario

  @property 
  def get_clave(self):
    return self.__clave
  @property 
  def get_tipo(self):
    return self.__tipo
  
  def tieneTarjeta(self):
    #ACCEDER A LA BDD, PEDIR TODAS LAS ULTIMAS 6 RESERVAS DEL USUARIO, VER LA ULTIMA FECHA Y QUE SEA MAYOR A 3 MESES
    self.__tieneTarjeta = True
    #UPADTE A LA BDD, PARA CAMBIAR EL ESTADO DEL CLIENTE QUE TIENE TARJETA
    
  def login(self):
    db = sqlite3.connect("cinemar.sqlite3")
    conexion = db.cursor()
    # nombreUsuario = input("Ingresa tu nombre de usuario: ")
    # contraseña = input("Ingresa tu contraseña: ")
    data = conexion.execute(f"SELECT nombre_usuario, contraseña, admin from usuario WHERE nombre_usuario = '{self.__nombre_usuario}' ")
    if(data):
      tuplaComparar = data.fetchone()
      if (tuplaComparar[1] == self.__clave):
        print("Acceso correcto")
    db.close()
  

