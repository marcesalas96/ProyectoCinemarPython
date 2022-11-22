class Pelicula :
    def __init__(self, id,  genero, descripcion, edad, duracion, titulo, idioma):
        self.__id = id
        self.__genero = genero
        self.__descripcion = descripcion
        self.__edad = edad
        self.__duracion = duracion
        self.__titulo = titulo
        self.__idioma = idioma
        
    def mostrarDatos(self):
        cadena= "\nTitulo: "+self.__titulo
        cadena+= "\nDescripcion: "+self.__descripcion
        cadena+= "\nDuracion: "+self.__duracion
        cadena+= "\nGenero: "+self.__genero
        cadena+= "\nApta para mayores de: "+self.__edad
        cadena+= "\nIdioma: "+self.__idioma
        return cadena
