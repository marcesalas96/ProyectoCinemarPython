class Usuario:

  def __init__(self, id_cliente='', nombre_usuario='', clave='', tipo=''):
    self.__nombre_usuario = nombre_usuario
    self.__clave = clave
    self.__tipo = tipo

  def __str__(self):
    cadena= "\nID_cliente: "+self.__id_cliente
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