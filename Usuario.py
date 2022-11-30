import sqlite3
class Usuario:

  def __init__(self, nombre_usuario='', clave=''):
    self.__nombre_usuario = nombre_usuario
    self.__clave = clave
    self.__tieneTarjeta = False

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
    tuplaComparar = data.fetchone()
    db.close()
    for elem in tuplaComparar:
      if(elem == self.__clave):
        pass
      else:
        return(print("Los datos ingresados no son validos"))
  
  def mostrarMenu(self):
    print(f"Bienvenido {self.__nombre_usuario} gracias por entrar al cine del grupo 4\n 1.Ver cartelera\n 2. Modificar reservas\n 3. Observar reservas\n 4. Ver historico de entradas")
    eleccion = input("Ingresa el numero de la opcion donde queres ir: ")
    db = sqlite3.connect("cinemar.sqlite3")
    conexion = db.cursor()
    if eleccion == 1:  
      salas = conexion.execute("SELECT * from salas")
      for sala in salas.fetchall():
        print(f"{sala[0]}. Pelicula : {sala[1]} Tipo: {sala[3]}")
      nroDeSala = input("Selecciona la peli que queres ver: ")
      if nroDeSala == 1 :
        pass
