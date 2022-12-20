import tkinter

import customtkinter
import os
from PIL import Image
from Class.Cliente import Cliente
from Class.Usuario import Usuario
from Class.Admin import Admin


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CINEMAR- GRUPO 4")
        self.geometry("600x400")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = r"C:\Users\marce\OneDrive\Escritorio\CursoPhyton\MilProgramadores\Cinemar\assets\images"
        # self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CINEMAR.png")), size=(500, 150))
        # self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Registrarse",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Ingresar",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure((1, 2), weight=1)
        self.second_frame.grid_rowconfigure((1,4), weight=0)
        
        self.nombre = customtkinter.CTkEntry(self.second_frame,placeholder_text="Ingresa tu nombre", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
        self.nombre.grid(row=1, column=1, pady=20)
        self.apellido = customtkinter.CTkEntry(self.second_frame,placeholder_text="Ingresa tu apellido", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
        self.apellido.grid(row=1, column=2,pady=20)
        self.correo = customtkinter.CTkEntry(self.second_frame,placeholder_text="Ingresa tu correo", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
        self.correo.grid(row=2, column=1,pady=20)
        self.edad = customtkinter.CTkEntry(self.second_frame,placeholder_text="Ingresa tu edad", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
        self.edad.grid(row=2, column=2,pady=20)
        self.nombre_usuario = customtkinter.CTkEntry(self.second_frame,placeholder_text="Ingresa tu nombre de usuario", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
        self.nombre_usuario.grid(row=3, column=1,pady=20)
        self.password = customtkinter.CTkEntry(self.second_frame,placeholder_text="Ingresa tu constraseña", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
        self.password.grid(row=3, column= 2,pady=20)
        self.buttonGuardar = customtkinter.CTkButton(self.second_frame, command=self.crearCliente, text="Registrarse")
        self.buttonGuardar.grid(row=4, column=2,pady=20)
        

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure((1, 2), weight=1)
        self.third_frame.grid_rowconfigure((1,2), weight=0)
        
        self.nombre_usuario = customtkinter.CTkEntry(self.third_frame,placeholder_text="Ingresa tu nombre de usuario", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
        self.nombre_usuario.grid(row=1, column=1,pady=20)
        self.password = customtkinter.CTkEntry(self.third_frame,placeholder_text="Ingresa tu constraseña", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
        self.password.grid(row=1, column= 2,pady=20)
        self.buttonGuardar = customtkinter.CTkButton(self.third_frame, command=self.logearse, text="Ingresar")
        self.buttonGuardar.grid(row=2, column=2,pady=20)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def crearCliente(self):
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        edad = self.edad.get()
        correo = self.correo.get()
        nombre_usuario = self.nombre_usuario.get()
        password = self.password.get()
        cliente = Cliente(nombre,apellido,correo,edad,nombre_usuario,password)
        cliente.registroUsuario()
        self.nombre.delete(0,len(nombre))
        self.apellido.delete(0,len(apellido))
        self.edad.delete(0,len(edad))
        self.correo.delete(0,len(correo))
        self.nombre_usuario.delete(0,len(nombre_usuario))
        self.password.delete(0,len(password))
        
    def logearse(self):
        nombre_usuario = self.nombre_usuario.get()
        password = self.password.get()
        usuario = Usuario(nombre_usuario, password)
        isAdmin = usuario.login()
        self.nombre_usuario.delete(0,len(nombre_usuario))
        self.password.delete(0,len(password))
        if(isAdmin):
            self.create_toplevel(nombre_usuario)
        else:
            self.create_menuUsuario(nombre_usuario, password)
        
    def create_toplevel(self, nombreUsuario):
        window = customtkinter.CTkToplevel(self)
        window.title("Panel de administrador")
        window.geometry("400x200")
        window.grid_columnconfigure((1,3), weight=0)
        window.grid_rowconfigure((1,6), weight=0)

        # create label on CTkToplevel window
        titulo = customtkinter.CTkLabel(window, text=f"Bienvenido {nombreUsuario}!", pady=10, padx=20)
        titulo.grid(row=1,column=2)
        combobox = customtkinter.CTkOptionMenu(master=window,values=["1. Crear Sala", "2. Crear Pelicula", "3. Crear Funcion", "4. Modificar Pelicula", "5. Ver Reservas"],command=self.optionmenu_callback)
        combobox.grid(row=2, column = 2)
        combobox.set("Elegi una opcion")    
    
    def create_menuUsuario(self, nombreUsuario):
        window = customtkinter.CTkToplevel(self)
        window.title("Panel de usuario")
        window.geometry("400x200")
        window.grid_columnconfigure((1,3), weight=0)
        window.grid_rowconfigure((1,6), weight=0)

        # create label on CTkToplevel window
        titulo = customtkinter.CTkLabel(window, text=f"Bienvenido {nombreUsuario}!", pady=10, padx=20)
        titulo.grid(row=1,column=2)
        combobox = customtkinter.CTkOptionMenu(master=window,values=["1. Ver Peliculas", "2. Mostrar Reservas"],command=self.optionmenu_callback)
        combobox.grid(row=2, column = 2)
        combobox.set("Elegi una opcion")    
        
    def optionmenu_callback(self,choice):
        if("1" in choice):
            windowCrearSalas = customtkinter.CTkToplevel(self)
            windowCrearSalas.title("Panel de administrador")
            windowCrearSalas.geometry("400x200")
            windowCrearSalas.grid_columnconfigure((1), weight=0)
            windowCrearSalas.grid_rowconfigure((1,3), weight=0)
            self.idSala = customtkinter.CTkEntry(windowCrearSalas,placeholder_text="Ingresa el numero de sala", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.idSala.grid(row=1, column=1,pady=20)
            self.cantidadButacas = customtkinter.CTkEntry(windowCrearSalas,placeholder_text="Ingresa la cantidad de butacas", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.cantidadButacas.grid(row=2, column= 1,pady=20)
            self.buttonGuardar = customtkinter.CTkButton(windowCrearSalas, command= self.crearSala,text="Guardar")
            self.buttonGuardar.grid(row=3, column=1,pady=20)
        elif("2" in choice):
            windowCrearPeli = customtkinter.CTkToplevel(self)
            windowCrearPeli.grid_columnconfigure((1, 2), weight=1)
            windowCrearPeli.grid_rowconfigure((1,6), weight=0)

            self.idPelicula = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa el numero de Pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.idPelicula.grid(row=1, column=1, pady=20)
            self.genero = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa tel genero de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.genero.grid(row=1, column=2,pady=20)
            self.descripcion = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa la descripcion de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.descripcion.grid(row=2, column=1,pady=20)
            self.edadPeli = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa la edad para ver la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.edadPeli.grid(row=2, column=2,pady=20)
            self.duracion = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa la duracion de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.duracion.grid(row=3, column=1,pady=20)
            self.titulo = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa el titulo de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.titulo.grid(row=3, column= 2,pady=20)
            self.tipo = customtkinter.CTkEntry(windowCrearPeli, placeholder_text="Ingresa el tipo de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.tipo.grid(row=4, column=1,pady=20)
            self.idioma = customtkinter.CTkEntry(windowCrearPeli, placeholder_text="Ingresa el idioma de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.idioma.grid(row=4, column=2,pady=20)
            self.sala = customtkinter.CTkEntry(windowCrearPeli, placeholder_text="Ingresa la sala de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.sala.grid(row=5, column=1,pady=20)
            self.botonGuardarPeli = customtkinter.CTkButton(windowCrearPeli, command=self.crearPeli, text="Guardar")
            self.botonGuardarPeli.grid(row=6, column=2,pady=20)
        elif("3" in choice):
            windowCrearFuncion = customtkinter.CTkToplevel(self)
            windowCrearFuncion.grid_columnconfigure((1, 2), weight=1)
            windowCrearFuncion.grid_rowconfigure((1,3), weight=0)
            self.idFuncion = customtkinter.CTkEntry(windowCrearFuncion,placeholder_text="Ingresa el numero de Funcion", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.idFuncion.grid(row=1, column=1, pady=20)
            self.horario = customtkinter.CTkEntry(windowCrearFuncion,placeholder_text="Ingresa el horario de la funcion", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.horario.grid(row=1, column=2,pady=20)
            self.fecha = customtkinter.CTkEntry(windowCrearFuncion,placeholder_text="Ingresa la fecha de la funcion", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.fecha.grid(row=2, column=1,pady=20)
            self.nroSala = customtkinter.CTkEntry(windowCrearFuncion,placeholder_text="Ingresa la sala de  la funcion", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.nroSala.grid(row=2, column=2,pady=20)
            self.botonGuardarFuncion = customtkinter.CTkButton(windowCrearFuncion, command=self.crearFuncion, text="Guardar")
            self.botonGuardarFuncion.grid(row=3, column=2,pady=20)
        elif("4" in choice):
            windowCrearPeli = customtkinter.CTkToplevel(self)
            windowCrearPeli.grid_columnconfigure((1, 2), weight=1)
            windowCrearPeli.grid_rowconfigure((1,6), weight=0)

            self.idPelicula = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa el numero de Pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.idPelicula.grid(row=1, column=1, pady=20)
            self.genero = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa tel genero de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.genero.grid(row=1, column=2,pady=20)
            self.descripcion = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa la descripcion de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.descripcion.grid(row=2, column=1,pady=20)
            self.edadPeli = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa la edad para ver la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.edadPeli.grid(row=2, column=2,pady=20)
            self.duracion = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa la duracion de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.duracion.grid(row=3, column=1,pady=20)
            self.titulo = customtkinter.CTkEntry(windowCrearPeli,placeholder_text="Ingresa el titulo de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.titulo.grid(row=3, column= 2,pady=20)
            self.tipo = customtkinter.CTkEntry(windowCrearPeli, placeholder_text="Ingresa el tipo de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.tipo.grid(row=4, column=1,pady=20)
            self.idioma = customtkinter.CTkEntry(windowCrearPeli, placeholder_text="Ingresa el idioma de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.idioma.grid(row=4, column=2,pady=20)
            self.sala = customtkinter.CTkEntry(windowCrearPeli, placeholder_text="Ingresa la sala de la pelicula", placeholder_text_color="white", width=300, height=25, border_width=2, corner_radius=10)
            self.sala.grid(row=5, column=1,pady=20)
            self.botonGuardarPeli = customtkinter.CTkButton(windowCrearPeli, command=self.actualizarPeli, text="Actualizar")
            self.botonGuardarPeli.grid(row=6, column=2,pady=20)
        else:
            windowVerReservas = customtkinter.CTkToplevel(self)
            windowVerReservas.geometry("800x900")
            windowVerReservas.grid_columnconfigure(1, weight=0)
            windowVerReservas.grid_rowconfigure((1, 100), weight=0)
            admin = Admin()
            reservas = admin.verReservas()
            contador = 2
            tituloReserva = customtkinter.CTkLabel(windowVerReservas, width=500, text="RESERVAS DE CLIENTES")
            tituloReserva.grid(row=1)
            
            for reserva in reservas:
                reservaLabel = customtkinter.CTkLabel(windowVerReservas, width=300, height=25, text=f"N°:{reserva[1]}, Hora: {reserva[2]}, Fecha: {reserva[3]}, Pelicula: {reserva[4]}, Fecha y Hora de reserva: {reserva[8]} - {reserva[9]}, Precio: ${reserva[7]}")
                reservaLabel.grid(row=contador, pady=10,padx=20)
                contador+=1
            
            
            
            
            
            
    def crearSala(self):
        admin = Admin()
        idSala = self.idSala.get()
        cantidadButacas = self.cantidadButacas.get()
        admin.crearSala(idSala, cantidadButacas)
    def crearPeli(self):
        admin = Admin()
        idPelicula = int(self.idPelicula.get())
        genero = self.genero.get()
        descripcion = self.descripcion.get() 
        edad = int(self.edadPeli.get())
        duracion = int(self.duracion.get())
        titulo = self.titulo.get()
        idioma = self.idioma.get()
        tipo = self.tipo.get()
        idSala = int(self.sala.get())
        admin.crearPelicula(idPelicula,genero,descripcion,edad,duracion,titulo,idioma,tipo,idSala)
    def crearFuncion(self):
        admin = Admin()
        idFuncion = int(self.idFuncion.get())
        horario = self.horario.get()
        fecha = self.fecha.get()
        idSala = int(self.nroSala.get())
        admin.crearFuncion(idFuncion, horario, fecha, idSala)
    def actualizarPeli(self):
        admin = Admin()
        idPelicula = int(self.idPelicula.get())
        genero = self.genero.get()
        descripcion = self.descripcion.get() 
        edad = int(self.edadPeli.get())
        duracion = int(self.duracion.get())
        titulo = self.titulo.get()
        idioma = self.idioma.get()
        tipo = self.tipo.get()
        idSala = int(self.sala.get())
        admin.actualizarPeli(idPelicula,genero,descripcion,edad,duracion,titulo,idioma,tipo,idSala)


