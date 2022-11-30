import tkinter as tk
import tkinter.font as tkFont
from Class.Usuario import Usuario

class App:
    def __init__(self, root):
        #setting title
        root.title("LogIn")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.__GLineEdit_387=tk.Entry(root)
        # self.__GLineEdit_387["anchor"] = "center"
        self.__GLineEdit_387["bg"] = "#ffffff"
        self.__GLineEdit_387["borderwidth"] = "1px"
        self.__GLineEdit_387["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        self.__GLineEdit_387["font"] = ft
        self.__GLineEdit_387["fg"] = "#333333"
        self.__GLineEdit_387["justify"] = "center"
        self.__GLineEdit_387["text"] = "Usuario"
        self.__GLineEdit_387.place(x=220,y=110,width=178,height=30)
        self.__GLineEdit_387["show"] = "Usuario"

        self.__GLineEdit_833=tk.Entry(root)
        self.__GLineEdit_833["bg"] = "#ffffff"
        self.__GLineEdit_833["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.__GLineEdit_833["font"] = ft
        self.__GLineEdit_833["fg"] = "#333333"
        self.__GLineEdit_833["justify"] = "center"
        self.__GLineEdit_833["text"] = "Contraseña"
        self.__GLineEdit_833["relief"] = "raised"
        self.__GLineEdit_833.place(x=220,y=170,width=178,height=30)

        GButton_932=tk.Button(root)
        GButton_932["bg"] = "#88817f"
        ft = tkFont.Font(family='Times',size=10)
        GButton_932["font"] = ft
        GButton_932["fg"] = "#ffffff"
        GButton_932["justify"] = "center"
        GButton_932["text"] = "INGRESAR"
        GButton_932["relief"] = "sunken"
        GButton_932.place(x=220,y=230,width=179,height=30)
        GButton_932["command"] = self.GButton_932_command

        GButton_797=tk.Button(root)
        GButton_797["bg"] = "#88817f"
        ft = tkFont.Font(family='Times',size=10)
        GButton_797["font"] = ft
        GButton_797["fg"] = "#ffffff"
        GButton_797["justify"] = "center"
        GButton_797["text"] = "CREAR CUENTA"
        GButton_797["relief"] = "sunken"
        GButton_797.place(x=220,y=280,width=178,height=30)
        GButton_797["command"] = self.GButton_797_command

        GLabel_622=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_622["font"] = ft
        GLabel_622["fg"] = "#333333"
        GLabel_622["justify"] = "center"
        GLabel_622["text"] = "INGRESA A TU CUENTA"
        GLabel_622.place(x=210,y=60,width=185,height=30)

    def GButton_932_command(self):
        nombre_usuario =  self.__GLineEdit_387.get()
        contraseña = self.__GLineEdit_833.get()
        usuario = Usuario(nombre_usuario, contraseña)
        usuario.login()
        
        


    def GButton_797_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
