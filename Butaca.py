class Butaca:
    def __init__(self, idSala, posicion):
        self.__idSala = idSala
        self.__posiscion = posicion
        self.__ocupado = False
    @property
    def getIdSala(self):
        return self.__idSala
    @property
    def getPosicion(self):
        return self.__posiscion
    @property
    def getOcupado(self):
        return self.__ocupado
    
    def actualizarOcupado(self):
        self.__ocupado = not self.__ocupado
        return "ocupado= "+ str(self.__ocupado)

    def mostrarDatos(self):
        cadena = "\nNumero de sala: "+ str(self.__idSala)
        cadena += "\nPosicion: "+ str(self.__posiscion)