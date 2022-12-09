import sqlite3
class Cliente:

  def __init__(self, nombre, apellido, correo, edad, nombre_usuario, contraseña):
    self.__nombre = nombre
    self.__apellido = apellido
    self.__correo = correo
    self.__edad = edad
    self.__admin = False
    self.__nombre_usuario = nombre_usuario
    self.__contraseña = contraseña
    self.__tiene_tarjeta = False

  def __str__(self):
    cadena= "\nNombre: "+self.__nombre
    cadena+= "\nApellido: "+self.__apellido
    cadena+= "\nCorreo: "+(self.__correo)
    cadena+= "\nEdad: "+str(self.__edad)
    return cadena

  @property 
  def get_nombre(self):
    return self.__nombre

  def set_nombre(self, nuevoNombre):
    self.__nombre=nuevoNombre
    return self.__nombre

  @property 
  def get_apellido(self):
    return self.__apellido

  def set_apellido(self, nuevoApellido):
    self.__apellido=nuevoApellido
    return self.__apellido

  @property 
  def get_correo(self):
    return self.__correo

  def set_correo(self, nuevoCorreo):
    self.__correo=nuevoCorreo
    return self.__correo 

  @property 
  def get_edad(self):
    return self.__edad

  def set_edad(self, nuevaEdad):
    self.__edad=nuevaEdad
    return self.__edad
  
  @property 
  def get_nombre_usuario(self):
    return self.__nombre_usuario
  
  @property 
  def get_contraseña(self):
    return self.__contraseña
  
  
  def registroUsuario(self):
    nombre = self.get_nombre 
    apellido = self.get_apellido
    edad = self.get_edad
    correo = self.get_correo
    nombreUsuario = self.get_nombre_usuario
    contraseña = self.get_contraseña
    db = sqlite3.connect("cinemar.sqlite3")
    conexion = db.cursor()
    conexion.execute(f"INSERT INTO usuario (nombre_usuario, contraseña, correo, admin, nombre, apellido, edad, tiene_tarjeta) VALUES ('{nombreUsuario}', '{contraseña}', '{correo}', '{self.__admin}', '{nombre}', '{apellido}', '{edad}', '{self.__tiene_tarjeta}')")
    db.commit()
    db.close()
  

