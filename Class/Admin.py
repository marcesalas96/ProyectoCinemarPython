import sqlite3
from Class.Sala import Sala
from Class.Pelicula import Pelicula
from Class.Funcion import Funcion
from Class.Butaca import Butaca
idFuncion = ""
class Admin:
    def __init__(self):
        pass
    def verReservas(self):
        db = sqlite3.connect("cinemar.sqlite3")
        conexion = db.cursor()
        data = conexion.execute(f"SELECT * FROM reserva")
        if(data):
            reservas = data.fetchall()
            db.commit()
            db.close()
        return reservas
    
    def verReservaParticular(self, usuarioCliente):
        db = sqlite3.connect("cinemar.sqlite3")
        conexion = db.cursor()
        dataCliente = conexion.execute(f"SELECT id_usuario FROM usuario where nombre_usuario = {usuarioCliente}")
        if(dataCliente):
            Cliente = dataCliente.fetchone()
            dataReserva = conexion.execute(f"SELECT * FROM reserva where id_cliente = {Cliente[0]}")
            if(dataReserva):
                reserva = dataReserva.fetchall()
                #mostrar reservas en interfaz grafica
            else:
                raise IndexError("No hay reservas para este usuario")    
        else:
            raise IndexError("No hay usuarios con este nombre de usuario")    
        db.commit()
        db.close()
    def crearSala(self, idSala, cantidadButacas):
        sala = Sala(idSala, cantidadButacas)
        sala.crearSalaBDD()
    def crearPelicula(self, idPelicula,genero,descripcion,edad,duracion,titulo,idioma,tipo,idSala):
        pelicula = Pelicula(idPelicula,genero,descripcion,edad,duracion,titulo,idioma,tipo,idSala)
        pelicula.guardarPeliculaBDD()
    def crearFuncion(self,idFuncion, horario, fecha, idSala ):
        funcion = Funcion(idFuncion, horario,fecha, idSala)
        funcion.guardarFuncionBDD()
        idFuncion = funcion.getId_Funcion()
        funcion.setButacas(self.crearButacas(idFuncion))
    def crearButacas(self, idFuncion):
        db = sqlite3.connect("cinemar.sqlite3")
        conexion = db.cursor()
        data = conexion.execute(f"SELECT id_sala from funcion WHERE id_funcion = {idFuncion}")
        if(data):
            idSala = data.fetchone()
            salaData = conexion.execute(f"SELECT * FROM sala WHERE id_sala = {int(idSala[0])}")
            cantidadDeButacas = salaData.fetchone()
            print(cantidadDeButacas)
            db.close()
            listaButacas = []
            for i in range(1, cantidadDeButacas[1] + 1):
                butaca = Butaca(idFuncion, i)
                butaca.guardarButacaBDD()
                listaButacas.append(butaca)
        return listaButacas
    def actualizarPeli(self,idPelicula,genero,descripcion,edad,duracion,titulo,idioma,tipo,idSala):
        pelicula = Pelicula(idPelicula,genero,descripcion,edad,duracion,titulo,idioma,tipo,idSala)
        pelicula.actualizarPeli()
        
        
        # def mostrarMenu(self):
        #     print("""***************************
        #     1. Crear Sala
        #     2. Crear Pelicula
        #     3. Crear Funcion
        #     4. Modificar Pelicula
        #     5. Ver Reservas
        #     *******************************""")
        #     seleccion = int(input("\n Ingresa la opcion donde quieras ingresar: "))
            
        #     if(seleccion == 1):
        #         idSala = input("Ingresa el numero de sala: ")
        #         cantidadButacas = input("Ingresa el numero de butacas de la sala: ")
        #         self.crearSala(idSala, cantidadButacas)
        #     elif(seleccion == 2):
        #         idPelicula = input("Ingresa el numero de pelicula: ")
        #         genero = input("Ingresa el genero de la pelicula: ")
        #         descripcion= input("Ingresa la descripcion de la pelicula: ")
        #         edad= input("Ingresa la edad necesaria para ver  la pelicula: ")
        #         duracion= input("Ingresa la duracion de la pelicula: ")
        #         titulo= input("Ingresa el titulo de la pelicula: ")
        #         idioma= input("Ingresa el idioma de la pelicula: ")
        #         tipo= input("Ingresa el tipo de la pelicula: ")
        #         numeroDeSala= input("Ingresa el numero de sala donde se va a proyectar la pelicula: ")
        #         self.crearPelicula(idPelicula, genero, descripcion, edad, duracion, titulo, idioma, tipo, numeroDeSala )
        #     elif (seleccion == 3):
        #         idFuncion = input("Ingresa el numero de funcion: ")
        #         horario= input("Ingresa el horario de la funcion: ")
        #         fecha= input("Ingresa la fecha de la pelicula: ")
        #         numeroDeSala= input("Ingresa el numero de sala donde se va a proyectar la pelicula: ")
        #         self.crearFuncion(idFuncion, horario, fecha, numeroDeSala)
        #     elif(seleccion == 4):
        #         idPelicula = input("Ingresa el numero de pelicula: ")
        #         genero = input("Ingresa el genero de la pelicula: ")
        #         descripcion= input("Ingresa la descripcion de la pelicula: ")
        #         edad= input("Ingresa la edad necesaria para ver  la pelicula: ")
        #         duracion= input("Ingresa la duracion de la pelicula: ")
        #         titulo= input("Ingresa el titulo de la pelicula: ")
        #         idioma= input("Ingresa el idioma de la pelicula: ")
        #         tipo= input("Ingresa el tipo de la pelicula: ")
        #         numeroDeSala= input("Ingresa el numero de sala donde se va a proyectar la pelicula: ")
        #         self.actualizarPeli(idPelicula, genero, descripcion, edad, duracion, titulo,idioma, tipo, numeroDeSala)
        #     elif(seleccion== 5):
        #         db = sqlite3.connect("cinemar.sqlite3")
        #         conexion = db.cursor()
        #         data = conexion.execute("SELECT * from reserva")
        #         reservas = data.fetchall()
        #         print("************Reservas************")
        #         for i in reservas:
        #             print(i)
                    # print("\n")
        