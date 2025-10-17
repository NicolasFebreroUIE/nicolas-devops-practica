import uuid
import datetime
from Models.Producto import Producto
from Models.Usuario import Cliente

# Solo defino clase de pedido con cada uno de los pedidos, no busco gestionarlos.

class Pedido:
    def __init__(self, cliente: Cliente):
        self.id_pedido = str(uuid.uuid4())
        self.cliente = cliente
        self.fecha = datetime.datetime.now()
        self.todos_Productos = []  # Aqui llamo a la lista de tuplas (producto, cantidad)

    def agregar_producto(self, producto: Producto, cantidad: int):
        if producto.hay_stock(cantidad):
            self.todos_Productos.append((producto, cantidad))
            producto.actualizar_stock(-cantidad)            
        else:
            print(f"No hay suficiente stock disponible para {producto.nombre}")
            

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.todos_Productos:
            total += producto.precio * cantidad
        return total

    def __str__(self):
        detalles_producto = ""
        for producto, cantidad in self.todos_Productos:
            detalles_producto += f" - {producto.nombre} x{cantidad} = ${producto.precio * cantidad}"

        return (f"Pedido ID: {self.id_pedido}"
                f"Fecha: {self.fecha.strftime('A-%m-%d %H:%M:%S')}"
                f"Cliente: {self.cliente.nombre} ({self.cliente.email})"
                f"Detalles: {detalles_producto}\n"
                f"Total: {self.calcular_total()}")
