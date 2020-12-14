class Producto():
    idproducto = 0
    nombre_Producto = ""
    precio = 0.0
    existencia = 0
    unidad_de_medidad = ""

    def printProduct(self):
        print(str(self.nombre_Producto) + " " + str(self.precio) + " " + str(self.existencia) + " " + str(self.unidad_de_medidad))

producto = Producto()
producto.idproducto = 1
producto.nombre_Producto = "Coca-Cola Retornable 2.5L"
producto.precio = 26.0
producto.existencia = 16
producto.unidad_de_medidad = "Botella"

producto.printProduct()