from tkinter import *
from tkinter import ttk

class Alumno:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Hola mundo")
        marco=LabelFrame(self.ventana,text="Alumno")
        marco.grid(row=0,column=0,columnspan=3,pady=20)
        #Nombre
        Label(marco,text="Nombre").grid(row=0,column=0)
        Entry(marco).grid(row=0,column=1)
        #Clave
        Label(marco,text="Clave").grid(row=1,column=0)
        Entry(marco).grid(row=1,column=1)
        #Boton
        ttk.Button(marco,text="Guardar alumno").grid(row=2,columnspan=2,sticky=W+E)
if __name__=="__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)
    ventana.mainloop()