from tkinter import *
from tkinter import ttk
import mariadb
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
        ttk.Button(marco,text="Guardar alumno",command=self.mostrarDatos).grid(row=2,columnspan=2,sticky=W+E)
        #Tabla
        self.tabla=ttk.Treeview(self.ventana,columns=2)
        self.tabla.grid(row=4,column=0,columnspan=2)
        self.tabla.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla.heading("#1",text="Clave",anchor=CENTER)

    def consulataAlumnos(self,query):
        try:
            conn=mariadb.connect(
                host="localhost",
                user="root",
                password="",
                database="escuela"
            )
        except mariadb.Error as e:
            print("Error al conectarse a la bd ",e)
        cur=conn.cursor()
        cur.execute(query)
        return cur
    def mostrarDatos(self):
        registros=self.tabla.get_children()
        for registro in registros:
            self.tabla.delete(registro)
        cur=self.consulataAlumnos("SELECT `nombre`,`clave` FROM `alumnos`")
        for (nombre,clave) in cur:
            self.tabla.insert('',0,text=nombre,values=clave)

if __name__=="__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)
    aplicacion.mostrarDatos()
    ventana.mainloop()