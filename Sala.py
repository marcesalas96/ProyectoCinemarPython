class Sala :
    def __init__(self,id, pelicula, butacas ):
        self.__id = id
        self.__pelicula = pelicula
        self.__butacas = (butacas)
    @property
    def getPelicula(self):
        return self.pelicula
    @property
    def getButacas(self):
        return self.__butacas
    @property
    def getId(self):
        return self.__id
    def mostrarDatos(self):
        cadena= "\nNumero de sala: "+ str(self.__id)
        cadena+= "\nPelicula en sala: "+self.__pelicula.mostrarDatos()
        cadena+= "\nCantidad de butacas: "+str(len(self.__butacas))
        return cadena