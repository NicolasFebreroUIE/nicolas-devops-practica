# Práctica 02 Arquitectura de software // Entregable
Nicolás Febrero Lubián

# Tienda Online en Python (POO)

Simulación didáctica de una tienda virtual desarrollada en Python utilizando Programación Orientada a Objetos. Permite crear usuarios, administrar productos y gestionar pedidos, manteniendo siempre actualizado el stock tras cada compra.

## Estructura del proyecto

- **`main.py`**  
  Script de ejemplo que crea la tienda, registra usuarios, añade productos al catálogo, simula varios pedidos y muestra por consola el catálogo, los pedidos y el stock actualizado tras las compras. :contentReference[oaicite:2]{index=2}  

- **`Producto.py`**  
  Define la clase base `Producto` y las subclases `ProductoElectronico` y `ProductoRopa`. Gestiona el identificador único de cada producto, su precio, el stock disponible y atributos específicos como garantía, talla o color. :contentReference[oaicite:3]{index=3}  

- **`Usuario.py`**  
  Contiene la clase base `Usuario` y las subclases `Cliente` y `Administrador`. Permite diferenciar entre usuarios normales y administradores, añadiendo datos como el código postal en clientes y permisos especiales en administradores. :contentReference[oaicite:4]{index=4}  

- **`Pedido.py`**  
  Implementa la clase `Pedido`, que relaciona un cliente con una lista de productos (y sus cantidades), calcula el total del pedido y genera un resumen legible con fecha, cliente y detalle de líneas de compra. :contentReference[oaicite:5]{index=5}  

- **`Tienda_service.py`**  
  Define la clase `TiendaService`, encargada de la lógica de negocio: gestión del catálogo, carrito, creación de pedidos, registro de usuarios, eliminación de productos por id y consulta del historial de pedidos por usuario. :contentReference[oaicite:6]{index=6}  


## Características principales

- Registro y diferenciación de usuarios: cliente y administrador.
- Catálogo editable con categorías de productos.
- Carrito de la compra que controla el stock en tiempo real.
- Pedidos asociados a cada cliente, con desglose de productos y cálculo automático.
- Historial de compras consultable por usuario.

