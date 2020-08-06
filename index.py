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
        self.nombre=Entry(marco)
        self.nombre.grid(row=0,column=1)
        self.nombre.focus()
        #Clave
        Label(marco,text="Clave").grid(row=1,column=0)
        self.clave=Entry(marco)
        self.clave.grid(row=1,column=1)
        #Boton
        self.crear=ttk.Button(marco,text="Crear alumno",command=self.agregarRegistro)
        self.crear.grid(row=2,columnspan=2,sticky=W+E)
        self.editar=ttk.Button(marco,text="Editar alumno",command=self.editarRegistro)
        self.editar.grid(row=3,columnspan=2,sticky=W+E)
        #Mensaje
        self.mensaje=Label(text='',fg='green')
        self.mensaje.grid(row=4,column=0,columnspan=2,sticky=W+E)
        #Tabla
        self.tabla=ttk.Treeview(self.ventana,columns=2)
        self.tabla.bind("<Double-Button-1>",self.doubleClickTabla)
        self.tabla.grid(row=5,column=0,columnspan=2)
        self.tabla.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla.heading("#1",text="Clave",anchor=CENTER)

    def queryAlumnos(self,query):
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
        cur=self.queryAlumnos("SELECT `nombre`,`clave` FROM `alumnos`")
        for (nombre,clave) in cur:
            self.tabla.insert('',0,text=nombre,values=clave)
    def agregarRegistro(self):
        if len(self.nombre.get())!=0 and len(self.clave.get())!=0:
            query="INSERT INTO `alumnos` (`id`, `nombre`, `clave`) VALUES (NULL, '"+self.nombre.get()+"', '"+self.clave.get()+"');"
            self.queryAlumnos(query)
            self.mensaje['text']="El alumno "+self.nombre.get()+" se a insertado exitosamente"
            self.nombre.delete(0,END)
            self.clave.delete(0,END)
            self.nombre.focus()
        else:
            self.mensaje['text']="El nombre y la clave del alumno no pueden estar vacias humano tonto"
        self.mostrarDatos()
    def editarRegistro(self):
        if len(self.nombre.get())!=0 and len(self.clave.get())!=0:
            query="UPDATE alumnos set nombre='"+self.nombre.get()+"',clave='"+self.clave.get()+"' where clave='"+self.claveVieja+"'; "
            self.queryAlumnos(query)
            self.mensaje['text']="El alumno "+self.nombre.get()+" se a actualizado exitosamente"
            self.nombre.delete(0,END)
            self.clave.delete(0,END)
            self.nombre.focus()
        else:
            self.mensaje['text']="El nombre y la clave del alumno no pueden estar vacias humano tonto"
        self.mostrarDatos()
        self.crear["state"]="normal"
        self.editar["state"]="disabled"
    def doubleClickTabla(self,event):
        self.claveVieja=str(self.tabla.item(self.tabla.selection())["values"][0])
        self.nombre.delete(0,END)
        self.clave.delete(0,END)
        self.crear["state"]="disable"
        self.editar["state"]="normal"
        self.nombre.insert(0,str(self.tabla.item(self.tabla.selection())["text"]))
        self.clave.insert(0,str(self.tabla.item(self.tabla.selection())["values"][0]))

if __name__=="__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)
    aplicacion.mostrarDatos()
    ventana.mainloop()