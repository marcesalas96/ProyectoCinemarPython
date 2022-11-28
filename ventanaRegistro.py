import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Registro")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_387=tk.Entry(root)
        GLineEdit_387["anchor"] = "center"
        GLineEdit_387["bg"] = "#ffffff"
        GLineEdit_387["borderwidth"] = "1px"
        GLineEdit_387["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_387["font"] = ft
        GLineEdit_387["fg"] = "#333333"
        GLineEdit_387["justify"] = "center"
        GLineEdit_387["text"] = "Nombre"
        GLineEdit_387.place(x=90,y=110,width=178,height=30)
        GLineEdit_387["show"] = "Usuario"

        GLineEdit_833=tk.Entry(root)
        GLineEdit_833["bg"] = "#ffffff"
        GLineEdit_833["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_833["font"] = ft
        GLineEdit_833["fg"] = "#333333"
        GLineEdit_833["justify"] = "center"
        GLineEdit_833["text"] = "Apellido"
        GLineEdit_833["relief"] = "raised"
        GLineEdit_833.place(x=290,y=110,width=178,height=30)

        GButton_932=tk.Button(root)
        GButton_932["bg"] = "#88817f"
        ft = tkFont.Font(family='Times',size=10)
        GButton_932["font"] = ft
        GButton_932["fg"] = "#ffffff"
        GButton_932["justify"] = "center"
        GButton_932["text"] = "REGISTRARSE"
        GButton_932["relief"] = "sunken"
        GButton_932.place(x=190,y=370,width=179,height=30)
        GButton_932["command"] = self.GButton_932_command

        GLabel_622=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_622["font"] = ft
        GLabel_622["fg"] = "#333333"
        GLabel_622["justify"] = "center"
        GLabel_622["text"] = "REGISTRATE COMO USUARIO DE CINEMAR"
        GLabel_622.place(x=60,y=60,width=291,height=30)

        GLineEdit_312=tk.Entry(root)
        GLineEdit_312["bg"] = "#ffffff"
        GLineEdit_312["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_312["font"] = ft
        GLineEdit_312["fg"] = "#333333"
        GLineEdit_312["justify"] = "center"
        GLineEdit_312["text"] = "Edad"
        GLineEdit_312.place(x=90,y=160,width=178,height=30)

        GLineEdit_945=tk.Entry(root)
        GLineEdit_945["bg"] = "#ffffff"
        GLineEdit_945["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_945["font"] = ft
        GLineEdit_945["fg"] = "#333333"
        GLineEdit_945["justify"] = "center"
        GLineEdit_945["text"] = "Correo Electrónico"
        GLineEdit_945.place(x=290,y=160,width=178,height=30)

        GLineEdit_344=tk.Entry(root)
        GLineEdit_344["bg"] = "#ffffff"
        GLineEdit_344["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_344["font"] = ft
        GLineEdit_344["fg"] = "#000000"
        GLineEdit_344["justify"] = "center"
        GLineEdit_344["text"] = "Usuario"
        GLineEdit_344.place(x=90,y=210,width=378,height=30)

        GLineEdit_609=tk.Entry(root)
        GLineEdit_609["bg"] = "#ffffff"
        GLineEdit_609["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_609["font"] = ft
        GLineEdit_609["fg"] = "#333333"
        GLineEdit_609["justify"] = "center"
        GLineEdit_609["text"] = "Contraseña"
        GLineEdit_609.place(x=90,y=260,width=180,height=30)

        GLineEdit_693=tk.Entry(root)
        GLineEdit_693["bg"] = "#ffffff"
        GLineEdit_693["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_693["font"] = ft
        GLineEdit_693["fg"] = "#333333"
        GLineEdit_693["justify"] = "center"
        GLineEdit_693["text"] = "Confirmar Contraseña"
        GLineEdit_693.place(x=290,y=260,width=175,height=30)

        GCheckBox_643=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_643["font"] = ft
        GCheckBox_643["fg"] = "#333333"
        GCheckBox_643["justify"] = "center"
        GCheckBox_643["text"] = "Quiero recibir novedades y promociones de Cinemar en mi correo"
        GCheckBox_643.place(x=100,y=320,width=372,height=30)
        GCheckBox_643["offvalue"] = "0"
        GCheckBox_643["onvalue"] = "1"
        GCheckBox_643["command"] = self.GCheckBox_643_command

    def GButton_932_command(self):
        print("command")


    def GCheckBox_643_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
