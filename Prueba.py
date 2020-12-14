from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



if __name__ == "__main__":
    window = Tk()
    window.title("Ventana Prueba")
    window.geometry('1200x720')

    wrapper1 = LabelFrame(window, text="Tabla de Productos")
    wrapper2 = LabelFrame(window, text="Añadir Productos")
    wrapper3 = LabelFrame(window, text="Hacer consulta")

    wrapper1.pack(fill="both", expand="yes", padx=20, pady=5)
    wrapper2.pack(fill="both", expand="yes", padx=20, pady=5)
    wrapper3.pack(fill="both", expand="yes", padx=20, pady=5)
    
    table = ttk.Treeview(wrapper1, columns=(1,2,3,4,5), show="headings", height="6")
    table.pack()

    table.heading(1, text="ID")
    table.heading(2, text="Nombre")
    table.heading(3, text="Precio")
    table.heading(4, text="Existencia")
    table.heading(5, text="Unidad de Medida")

    window.mainloop()