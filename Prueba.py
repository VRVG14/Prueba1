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
    consulta = "SELECT * FROM Producto WHERE nombreProducto LIKE %" + palabra + "%"
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
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=5)
    wrapper3.pack(fill="both", expand="yes", padx=20, pady=5)
    
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
    label.pack(side=tk.LEFT, padx=10)
    entry = Entry(wrapper2, textvariable=txtBuscar)
    entry.pack(side=tk.LEFT, padx=5)
    btn = Button(wrapper2, text='Buscar', command=buscar)
    btn.pack(side=tk.LEFT, padx=6)
    
    
    pito = query("SELECT * FROM Producto;")
    actualizarTabla(pito)

    window.mainloop()