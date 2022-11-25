class Cliente:

  def __init__(self, nombre='', apellido='', correo='', edad='', id_cliente=''):
    self.__nombre = nombre
    self.__apellido = apellido
    self.__correo = correo
    self.__edad = edad
    self.__id_cliente = id_cliente

  def __str__(self):
    cadena= "\nNombre: "+self.__nombre
    cadena+= "\nApellido: "+self.__apellido
    cadena+= "\nCorreo: "+(self.__correo)
    cadena+= "\nEdad: "+str(self.__edad)
    cadena+= "\nID_cliente: "+str(self.__id_cliente)
    return cadena

  @property 
  def get_nombre(self):
    return self.__nombre

  def set_nombre(self, nuevoNombre):
    self.__nombre=nuevoNombre
    return self.__nombre

  @property 
  def get_apellido(self):
    return self.__apellido

  def set_apellido(self, nuevoApellido):
    self.__apellido=nuevoApellido
    return self.__apellido

  @property 
  def get_correo(self):
    return self.__correo

  def set_correo(self, nuevoCorreo):
    self.__correo=nuevoCorreo
    return self.__correo 

  @property 
  def get_edad(self):
    return self.__edad

  def set_edad(self, nuevaEdad):
    self.__edad=nuevaEdad
    return self.__edad

  @property 
  def get_id_cliente(self):
    return self.__id_cliente

  def set_id_cliente(self, nuevo_id_cliente):
    self.__id_cliente=nuevo_id_cliente
    return self.__id_cliente

  def registro_usuario(self):

    self.__nombre = self.get_nombre()
    self.__apellido = self.get_apellido()
    self.__correo = self.get_correo()
    self.__edad = self.get_edad()
    self.__id_cliente = self.get_id_cliente()

    # conexión
    if self.__nombre != '' and self.__apellido != '' and self.__correo != '' and self.__edad != '' and self.__id_cliente != '' :
        pass
    # esta correcto
    else:
        messagebox.showerror(title = 'ERROR', message = 'Para continuar, complete todos los datos solicitados')
        return

    db = sqlite3.connect('Cinemar.db')
    conexion = db.cursor()

    # verificación 
    conexion.execute('SELECT * FROM cliente WHERE cliente = ?', [])

    if conexion.fetchone():
        messagebox.showerror(title = 'ERROR', message = 'El usuario ingresado ya existe. Intente nuevamente.')
    else:
        conexion.execute('INSERT INTO cliente VALUES(NULL,?,?,?,?,?,?,5)',(nombre, apellido, correo, edad, idCliente))
        db.commit()
        self.set_nombre('')
        self.set_apellido('')
        self.set_correo('')
        self.set_edad('')
        self.set_id_cliente('')


    # Conexión cerrada
    conexion.close()
    db.close()
