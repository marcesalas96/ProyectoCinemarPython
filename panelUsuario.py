import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Panel Usuario")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_932=tk.Button(root)
        GButton_932["bg"] = "#88817f"
        ft = tkFont.Font(family='Times',size=10)
        GButton_932["font"] = ft
        GButton_932["fg"] = "#ffffff"
        GButton_932["justify"] = "center"
        GButton_932["text"] = "HACER UNA RESERVA"
        GButton_932["relief"] = "sunken"
        GButton_932.place(x=20,y=120,width=134,height=30)
        GButton_932["command"] = self.GButton_932_command

        GLabel_622=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_622["font"] = ft
        GLabel_622["fg"] = "#333333"
        GLabel_622["justify"] = "center"
        GLabel_622["text"] = "BIENVENIDO A CINEMAR"
        GLabel_622.place(x=20,y=30,width=152,height=30)

        GMessage_919=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_919["font"] = ft
        GMessage_919["fg"] = "#333333"
        GMessage_919["justify"] = "center"
        GMessage_919["text"] = "Seleccione la acción que desea realizar"
        GMessage_919.place(x=0,y=70,width=263,height=30)

        GButton_18=tk.Button(root)
        GButton_18["bg"] = "#88817f"
        ft = tkFont.Font(family='Times',size=10)
        GButton_18["font"] = ft
        GButton_18["fg"] = "#ffffff"
        GButton_18["justify"] = "center"
        GButton_18["text"] = "VER MIS RESERVAS"
        GButton_18.place(x=170,y=120,width=134,height=30)
        GButton_18["command"] = self.GButton_18_command

        GButton_258=tk.Button(root)
        GButton_258["bg"] = "#88817f"
        ft = tkFont.Font(family='Times',size=10)
        GButton_258["font"] = ft
        GButton_258["fg"] = "#ffffff"
        GButton_258["justify"] = "center"
        GButton_258["text"] = "MODIFICAR MI RESERVA"
        GButton_258.place(x=320,y=120,width=143,height=30)
        GButton_258["command"] = self.GButton_258_command

    def GButton_932_command(self):
        print("command")


    def GButton_18_command(self):
        print("command")


    def GButton_258_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
