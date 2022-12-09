class Descuento:
    def __init__ (self, tipoDePelicula, tieneTarjeta, dia):
        self.__tipo = tipoDePelicula
        self.__tarjeta = tieneTarjeta
        self.__precioEntrada = 0
        self.__dia = dia
        self.__porcentajeDescuento = 0
        
    # def setValorEntrada(self):
            
    def valorEntrada(self):
        if(self.__tipo == "2D"):
            self.__tarjeta = 300
        else:
            self.__tarjeta = 400  
            
    def porcentajeDescuento(self):
        if(self.__dia == "MARTES" || "" )