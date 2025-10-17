from Services.Tienda_service import TiendaService 
from Models.Producto import Producto, ProductoElectronico, ProductoRopa

def main():
    tienda = TiendaService()

    # Aquí registro algunos usuarios de ejemplo
    cliente1 = tienda.registrar_usuario("cliente", "Nicolás Febrero", "nicolas02@email.com", "36201")
    cliente2 = tienda.registrar_usuario("cliente", "Miguel Ángel", "Miguel@email.com", "36202")
    cliente3 = tienda.registrar_usuario("cliente", "Sergio Arca", "Sergio.A@email.com", "36203")
    admin1   = tienda.registrar_usuario("admin", "Admin Principal", "admin@email.com")

    # Estos son los productos que voy a añadir al inventario como ejemplos
    p1 = Producto("Chicles", 1.2, 50)
    p2 = ProductoElectronico("Lavadora", 25, 10, 12)
    p3 = ProductoRopa("Camisa", 15, 30, "M", "Lino fino")
    p4 = Producto("Leche", 0.9, 40)
    p5 = ProductoElectronico("Iphone17 pro", 45, 5, 24)

    # Añadir al inventario
    tienda.agregar_producto(p1)
    tienda.agregar_producto(p2)
    tienda.agregar_producto(p3)
    tienda.agregar_producto(p4)
    tienda.agregar_producto(p5)

    print("-- Inventario inicial previo a las compras: --")
    tienda.listar_productos()

    
    # Resultado tras realizar los pedidos
    
    print("-- Realización de los pedidos... --")
    pedido1 = tienda.realizar_pedido(cliente1.id_usuario, [(p1.id_producto, 2), (p3.id_producto, 1)])
    pedido2 = tienda.realizar_pedido(cliente2.id_usuario, [(p2.id_producto, 1), (p4.id_producto, 3)])
    pedido3 = tienda.realizar_pedido(cliente3.id_usuario, [(p5.id_producto, 2), (p1.id_producto, 5)])

    
    # Muestra los pedidos de un cliente como confimración de que se ha hecho correctamente
    
    print(" Lista de pedidos previos del cliente Juan Pérez:")
    tienda.listar_pedidos_usuario(cliente1.id_usuario)
    print(" Lista de pedidos previos del cliente Laura Gomez:")
    tienda.listar_pedidos_usuario(cliente2.id_usuario)
    print(" Lista de pedidos previos del cliente Carlos Ruiz:")
    tienda.listar_pedidos_usuario(cliente3.id_usuario)

    
    # Stock actualizado una vez que los pedidos se han tramitado    
    print(" Stock actualizado después de los pedidos:")
    tienda.listar_productos()


if __name__ == "__main__":
    main()
