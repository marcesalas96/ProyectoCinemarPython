# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import sys
sys.path.append(r"C:\Users\marce\OneDrive\Escritorio\CursoPhyton\MilProgramadores\Cinemar")

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\marce\OneDrive\Escritorio\CursoPhyton\MilProgramadores\Cinemar\build\assets\frame3"
)


class Reserva():
    
    def __init__(self, master):
        super().__init__(master)
        self.__master = master
        self.crearWidget()

    def relative_to_assets( self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def crearWidget(self):
        self.__master.geometry("1280x832")
        self.__master.configure(bg="#FFFFFF")
        self.__master.resizable(False, False)
        
        canvas = Canvas(
            self.__master,
            bg="#FFFFFF",
            height=832,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(0.0, 0.0, 571.0, 832.0, fill="#1B2D50", outline="")

        canvas.create_text(
            81.0,
            238.0,
            anchor="nw",
            text="VIVÍ LA EXPERIENCIA",
            fill="#FFFFFF",
            font=("Inter", 30 * -1),
        )

        canvas.create_text(
            81.0,
            372.0,
            anchor="nw",
            text="CINEMAR",
            fill="#FFFFFF",
            font=("AllertaStencil Regular", 95 * -1),
        )

        canvas.create_text(
            640.0,
            114.0,
            anchor="nw",
            text="HACÉ TU RESERVA",
            fill="#000000",
            font=("Inter", 27 * -1),
        )

        button_image_1 = PhotoImage(file= self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
        )
        button_1.place(
            x=695.3292236328125, y=219.0, width=410.6707763671875, height=74.0
        )

        button_image_2 = PhotoImage(file= self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
        )
        button_2.place(x=695.0, y=345.0, width=411.0, height=74.0)

        button_image_3 = PhotoImage(file= self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat",
        )
        button_3.place(x=695.0, y=470.0, width=411.0, height=74.0)

        canvas.create_text(
            712.0,
            582.0,
            anchor="nw",
            text="Ingresá tu N° de Socio",
            fill="#000000",
            font=("Inter Bold", 20 * -1),
        )

        entry_image_1 = PhotoImage(file= self.relative_to_assets("entry_1.png"))
        # entry_bg_1 = canvas.create_image(906.5, 663.0, image=entry_image_1)
        entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry_1.place(x=738.0, y=626.0, width=337.0, height=72.0)

        button_image_4 = PhotoImage(file= self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat",
        )
        button_4.place(x=992.0, y=750.0, width=227.0, height=82.0)
        # self.mainloop()