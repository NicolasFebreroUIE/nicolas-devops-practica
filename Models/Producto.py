import random as rd

# Sigo la misma idea que en usuario, defino clase producto y luego subclases para tipos de productos. 
# Además dentro de la clase producto defino métodos para gestionar el stock.


# Defino clase producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.id_producto = rd.randint(1, 50)
        self.nombre = nombre
        self.precio = precio
        self.__stock = stock  # Atributo privado

    # Consultar stock
    def consultar_stock(self):
        return self.__stock

    # Actualizar stock (positivo para reponer, negativo para venta) // no utilizo el return porque no me hace falta en este caso (true/false)
    def actualizar_stock(self, cantidad):
        if self.__stock + cantidad < 0:
            print(f"No hay suficiente stock de {self.nombre}. Stock actual: {self.__stock}")            
        self.__stock += cantidad
        

    # Consultar si hay suficiente stock para una cantidad
    def hay_stock(self, cantidad):
        return self.__stock >= cantidad

    # Este print lo uso en tienda_service para listar productos
    def __str__(self):
        return f"ID: {self.id_producto} | {self.nombre} | Precio: {self.precio} | Stock: {self.__stock}"


# Subclase para el producto electrónico con variables.
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, precio, stock)
        self.garantia_meses = garantia_meses

    def __str__(self):
        return f"{super().__str__()} | Garantía: {self.garantia_meses} meses"


# Subclase producto ropa
class ProductoRopa(Producto):
    def __init__(self, nombre, precio, stock, talla, color):
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color

    def __str__(self):
        return f"{super().__str__()} | Talla: {self.talla} | Color: {self.color}"
