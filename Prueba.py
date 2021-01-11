from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Intermediario

def actualizarTabla(lista):
    """
    Metodo para actualizar la tabla
    Recibe como parametro una Lista de objetos
    """
    table.delete(*table.get_children())
    id = 1
    for i in lista:
        table.insert('', 'end',values=i)
        table.column(id, anchor=tk.N)
        id += 1

def query(query):
    """
    Funcion para hacer una consulta
    tiene como parametro una variable string para hacer las consultas
    """
    inter = Intermediario.Consultas()
    result = inter.querySimok(query)
    return result

def buscar():
    """
    Comando usador por el btn buscar, para poder el producto escrito por el usuario
    """
    palabra = txtBuscar.get()
    if comboEleccion.current() == -1:
        consulta = "SELECT * FROM Producto WHERE nombreProducto LIKE '%" + palabra + "%'"
    elif comboEleccion.current() == 0:
        consulta = "SELECT * FROM Producto WHERE ID LIKE '%" + palabra + "%'"
    elif comboEleccion.current() == 1:
        consulta = "SELECT * FROM Producto WHERE nombreProducto LIKE '%" + palabra + "%'"
    elif comboEleccion.current() == 2:
        consulta = "SELECT * FROM Producto WHERE Proveedor LIKE '%" + palabra + "%'"
    elif comboEleccion.current() == 3:
        consulta = "SELECT * FROM Producto WHERE precio LIKE '%" + palabra + "%'"
    elif comboEleccion.current() == 4:
        consulta = "SELECT * FROM Producto WHERE existencia LIKE '%" + palabra + "%'"
    
    actualizarTabla(query(consulta))

if __name__ == "__main__":
    window = Tk()
    txtBuscar = StringVar()
    window.title("Ventana Prueba")
    window.geometry('1200x720')

    wrapper1 = LabelFrame(window, text="Tabla de Productos")
    wrapper2 = LabelFrame(window, text="Añadir Productos")
    wrapper3 = LabelFrame(window, text="Hacer consulta")

    wrapper1.pack(fill="both", expand="yes", padx=5, pady=5)
    wrapper2.pack(fill="both", expand="yes", padx=5, pady=5)
    wrapper3.pack(fill="both", expand="yes", padx=5, pady=5)
    
    table = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6), show="headings", height="6")
    table.pack()

    table.heading(1, text="ID")
    table.heading(2, text="Nombre")
    table.heading(3, text="Proveedor")
    table.heading(4, text="Precio")
    table.heading(5, text="Existencia")
    table.heading(6, text="Unidad de Medida")
    
    #Buscar
    label = Label(wrapper2, text='Buscar')
    label.place(x=3,y=3)
    entry = Entry(wrapper2, textvariable=txtBuscar)
    entry.place(x=3,y=23)
    btn = Button(wrapper2, text='Buscar', command=buscar)
    btn.place(x=173,y=20)
    comboEleccion = ttk.Combobox(wrapper2, state="readonly", values=["ID","Nombre","Proveedor","Precio","Existencia"])
    comboEleccion.place(x=3,y=50, width=239)

    
    
    pito = query("SELECT * FROM Producto;")
    actualizarTabla(pito)

    window.mainloop()