import sqlite3

class Pelicula :
    def __init__(self, id,  genero, descripcion, edad, duracion, titulo, idioma, tipo, nroSala):
        self.__id = id
        self.__genero = genero
        self.__descripcion = descripcion
        self.__edad = edad
        self.__duracion = duracion
        self.__titulo = titulo
        self.__idioma = idioma
        self.__tipo = tipo
        self.__nroSala = nroSala
        
    def mostrarDatos(self):
        cadena= "\nTitulo: "+self.__titulo
        cadena+= "\nDescripcion: "+self.__descripcion
        cadena+= "\nDuracion: "+self.__duracion
        cadena+= "\nGenero: "+self.__genero
        cadena+= "\nApta para mayores de: "+self.__edad
        cadena+= "\nIdioma: "+self.__idioma
        return cadena
    def guardarPeliculaBDD(self):
        bd = sqlite3.connect("cinemar.sqlite3")
        conexion = bd.cursor()
        conexion.execute(f"INSERT INTO pelicula (titulo, duracion, idioma, edad, descripcion, genero, tipo, id_sala) VALUES ('{self.__titulo}',{self.__duracion},'{self.__idioma}',{self.__edad},'{self.__descripcion}','{self.__genero}','{self.__tipo}',{self.__nroSala})")
        bd.commit()
        bd.close()
        