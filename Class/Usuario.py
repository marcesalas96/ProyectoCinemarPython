import sqlite3
from Class.Admin import Admin
from Class.Reserva import Reserva
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
  def mostrarMenu(self):
    print(f"BIENVENIDO A CINEMAR, {self.__nombre_usuario}")
    print("""
          1. Ver Peliculas
          2. Mostrar Reservas""")
    seleccion = int(input("Ingresa la opcion: "))
    if(seleccion== 1):
      self.mostrarPeliculas()
    elif(seleccion == 2):
      self.mostrarReservas()
  def mostrarPeliculas(self):
    db = sqlite3.connect("cinemar.sqlite3")
    conexion = db.cursor()
    data = conexion.execute("SELECT funcion.id_funcion, funcion.horario, funcion.fecha, pelicula.titulo, pelicula.duracion, pelicula.tipo FROM sala INNER JOIN pelicula ON pelicula.id_sala = sala.id_sala INNER JOIN funcion ON funcion.id_sala = sala.id_sala ")
    tupla = data.fetchall()
    print(f"\n{self.__nombre_usuario}, estas son las peliculas que tenemos para ofrecerte!\n")
    for peli in tupla:
      print(peli)
    seleccion = input("\nSelecciona la peli que queres ver: ")
    self.crearReserva(seleccion, tupla)
    
  def login(self):
    db = sqlite3.connect("cinemar.sqlite3")
    conexion = db.cursor()
    data = conexion.execute(f"SELECT nombre_usuario, contraseña, admin from usuario WHERE nombre_usuario = '{self.__nombre_usuario}' ")
    if(data):
      tuplaComparar = data.fetchone()
      if (tuplaComparar[1] == self.__clave):
        if(tuplaComparar[2] == "True"):
          db.close() 
          admin = Admin(self.__nombre_usuario)
          admin.mostrarMenu()
        else:
          self.mostrarMenu()
        #abriria ventana de panel de usuario 
    
  def crearReserva(self, seleccion, tupla):
    db = sqlite3.connect("cinemar.sqlite3")
    conexion = db.cursor()
    data = conexion.execute(f"SELECT id_usuario from usuario WHERE nombre_usuario = '{self.__nombre_usuario}'")
    idUsuario = data.fetchone()
    reserva = Reserva(tupla[int(seleccion) - 1 ], idUsuario[0])
    reserva.crearReserva()
    
  def mostrarReservas(self):
    db = sqlite3.connect("cinemar.sqlite3")
    conexion = db.cursor()
    data = conexion.execute(f"SELECT id_usuario from usuario WHERE nombre_usuario = '{self.__nombre_usuario}'")
    idUsuario = data.fetchone()
    dataReservas = conexion.execute(f"SELECT * from reserva WHERE id_usuario = {idUsuario[0]}")
    reservas = dataReservas.fetchall()
    for reserva in reservas:
      print(reserva)
      print("\n")
    db.commit()
    db.close()
    


