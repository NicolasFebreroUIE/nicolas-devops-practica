from Models.Producto import Producto, ProductoElectronico, ProductoRopa
from Models.Usuario import Cliente, Admin
from Models.Pedido import Pedido

class TiendaService:
    def __init__(self):
        # La tienda guarda en memoria todos los productos, usuarios y pedidos
        self.productos = []
        self.usuarios = []
        self.pedidos = []

    # Para la gestion de usuarios defino dos  funciones, una para registrar y otra para buscar.
    def registrar_usuario(self, tipo: str, nombre: str, email: str, codigo_postal=None):
        # Crea un Cliente o un Admin dependiendo del parámetro "tipo"
        if tipo.lower() == "cliente":
            usuario = Cliente(nombre, email, codigo_postal)
        elif tipo.lower() == "admin":
            usuario = Admin(nombre, email)
        else:
            raise ValueError("Tipo de usuario no válido. Usa 'cliente' o 'admin'.")
        
        # Guarda el usuario en la lista
        self.usuarios.append(usuario)
        print(f"Usuario registrado: {usuario.nombre} ({'Admin' if usuario.is_admin() else 'Cliente'})")
        return usuario

    def buscar_usuario(self, id_usuario: int):
        # Busca un usuario por su id
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    #Para la gestión de productos defino cuatro funciones, una para agregar, otra para eliminar, otra para listar y otra para buscar.
    def agregar_producto(self, producto: Producto):
        # Agrega un producto al inventario
        self.productos.append(producto)
        print(f"Producto agregado: {producto}")

    def eliminar_producto(self, id_producto: int):
        # Elimina un producto del inventario por su id
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                print(f"Producto eliminado: {producto.nombre}")
                
        print("Nombre o códgio de producto no encontrado.")
        

    def listar_productos(self):
        # Muestra todos los productos disponibles
        if not self.productos:
            print("No hay productos dsiponibles en la tienda.")
        for producto in self.productos:
            print(producto)

    def buscar_producto(self, id_producto: int):
        # Busca un producto por su id
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto
        return None

   # Para la gestión de pedidos defino tres funciones, una para realizar pedidos, otra para listar los pedidos de un usuario y otra para listar todos los pedidos.
    def realizar_pedido(self, id_usuario: int, productos_solicitados: list):
        """
        productos_solicitados: lista de tuplas (id_producto, cantidad)
        """
        # Verifica que el usuario exista
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            print("El usuario buscado no existe, por favor revise que esté bien escrito.")
            return None

        # Crea un pedido nuevo para ese usuario
        pedido = Pedido(usuario)

        # Recorre los productos solicitados y verifica stock
        for id_producto, cantidad in productos_solicitados:
            producto = self.buscar_producto(id_producto)
            if not producto:
                print(f"El producto con el ID {id_producto} no encontrado.")
                return None
            if not producto.hay_stock(cantidad):
                print(f"No hay stock suficiente para {producto.nombre}.")
                return None
            pedido.agregar_producto(producto, cantidad)

        # Si todo va bien, guarda el pedido en la lista de pedidos
        self.pedidos.append(pedido)
        print(f"Pedido realizado correctamente. ID: {pedido.id_pedido}")
        return pedido

    def listar_pedidos_usuario(self, id_usuario: int):
        # Muestra todos los pedidos de un usuario específico, ordenados por fecha
        pedidos_usuario = [p for p in self.pedidos if p.cliente.id_usuario == id_usuario]
        pedidos_usuario.sort(key=lambda p: p.fecha)  
        if not pedidos_usuario:
            print("El usuario no tiene pedidos.")
        for pedido in pedidos_usuario:
            print(pedido)

    def listar_pedidos(self):
        """Muestra todos los pedidos registrados en la tienda, ordenados por fecha."""
        if not self.pedidos:
            print("No hay pedidos registrados.")
            return
        pedidos_ordenados = sorted(self.pedidos, key=lambda p: p.fecha)
        for pedido in pedidos_ordenados:
            print(pedido)
