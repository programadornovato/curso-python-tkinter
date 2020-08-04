from tkinter import *

class Alumno:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Hola mundo")
        
if __name__=="__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)
    ventana.mainloop()