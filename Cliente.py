class Cliente:

  def __init__(self, nombre='', apellido='', correo='', edad='', id_cliente=''):
    self.__nombre = nombre
    self.__apellido = apellido
    self.__correo = correo
    self.__edad = edad
    self.__id_cliente = id_cliente

  def __str__(self):
    cadena= "\nNombre: "+self.__nombre
    cadena+= "\nApellido: "+self.__apellido
    cadena+= "\nCorreo: "+(self.__correo)
    cadena+= "\nEdad: "+str(self.__edad)
    cadena+= "\nID_cliente: "+str(self.__id_cliente)
    return cadena

  @property 
  def get_nombre(self):
    return self.__nombre

  @property 
  def get_apellido(self):
    return self.__apellido

  @property 
  def get_correo(self):
    return self.__correo

  @property 
  def get_edad(self):
    return self.__edad

  @property 
  def get_id_cliente(self):
    return self.__id_cliente
