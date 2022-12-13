from Class.Cliente import Cliente
from Class.Usuario import Usuario
from Class.clase_descuento import Descuento
from datetime import datetime
# cliente = Cliente("marce", "salas","marce@gmail.com", 26,"msalas1","msalas1")
# cliente.setAdmin()
# cliente.registroUsuario()
usuario = Usuario("msalas1", "msalas1")
usuario.login()

# d = datetime.now()
# dia = d.weekday()
# descuento = Descuento("2D", False, str(dia))
# valor = descuento.porcentajeDescuento()
# print(valor)