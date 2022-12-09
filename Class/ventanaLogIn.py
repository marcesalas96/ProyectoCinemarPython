import sys
sys.path.append(r"C:\Users\marce\OneDrive\Escritorio\CursoPhyton\MilProgramadores\Cinemar")
from Class.vetanaReserva import Registro
from pathlib import Path
from tkinter import *
from Class.Usuario import Usuario

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\marce\OneDrive\Escritorio\CursoPhyton\MilProgramadores\Cinemar\build\assets\frame0")


    
def abrirVentana():
    registro = Registro(Tk())
    nuevaVentana = Toplevel(registro)

def loginUsuario(nombreUsuario, contraseña):
    usuario = Usuario(nombreUsuario, contraseña)
    usuario.login()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()
window.geometry("1280x832")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    571.0,
    832.0,
    fill="#1B2D50",
    outline="")
canvas.create_text(
    65.0,
    236.99999999999994,
    anchor="nw",
    text="BIENVENIDO A ",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)
canvas.create_text(
    640.0,
    77.99999999999994,
    anchor="nw",
    text="INGRESÁ A TU CUENTA",
    fill="#000000",
    font=("Inter", 27 * -1)
)
canvas.create_text(
    670.0,
    601.0,
    anchor="nw",
    text="¿NO TENÉS CUENTA?",
    fill="#000000",
    font=("Inter", 20 * -1)
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=763.0,
    y=499.99999999999994,
    width=278.0,
    height=47.0
)
canvas.create_text(
    670.0,
    150.99999999999994,
    anchor="nw",
    text="USUARIO",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)
canvas.create_text(
    65.0,
    370.99999999999994,
    anchor="nw",
    text="CINEMAR",
    fill="#FFFFFF",
    font=("AllertaStencil Regular", 95 * -1)
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    912.0,
    211.99999999999994,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=665.0,
    y=186.99999999999994,
    width=494.0,
    height=48.0
)
canvas.create_text(
    670.0,
    264.99999999999994,
    anchor="nw",
    text="CONTRASEÑA",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    909.0,
    335.99999999999994,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=662.0,
    y=310.99999999999994,
    width=494.0,
    height=48.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= lambda : loginUsuario(entry_1.get(), entry_2.get()),
    relief="flat"
)
button_2.place(
    x=741.0,
    y=400.99999999999994,
    width=300.0,
    height=79.0
)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command= lambda : ,
    relief="flat"
)
button_3.place(
    x=735.0,
    y=668.0,
    width=300.0,
    height=74.0
)
canvas.create_rectangle(
    650.0,
    572.0,
    1153.0,
    573.0,
    fill="#000000",
    outline="")

window.resizable(False, False)
window.mainloop()



