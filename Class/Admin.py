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
        data = conexion.execute(f"SELECT * FROM reservas")
        if(data):
            reservas = data.fetchall()
            #mostrar reservas en interfaz grafica
        db.commit()
        db.close()
    def verReservaParticular(self, usuarioCliente):
        db = sqlite3.connect("cinemar.sqlite3")
        conexion = db.cursor()
        dataCliente = conexion.execute(f"SELECT id_usuario FROM usuario where nombre_usuario = {usuarioCliente}")
        if(dataCliente):
            Cliente = dataCliente.fetchone()
            dataReserva = conexion.execute(f"SELECT * FROM reservas where id_cliente = {Cliente[0]}")
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