import random as rd

# Defino clase usuario,  cliente como clase de Usuario y admin como clase de usuario, a diferencia de pedido, prefiero generar tres clases diferentes pero manteniendo cliente y usuario como clases de usuario.
class Usuario:
    def __init__(self, nombre, email):
        self.id_usuario = rd.randint(1, 1000)
        self.nombre = nombre
        self.email = email

    def is_admin(self):
        return False

# Subclase cliente definidad como clase.
class Cliente(Usuario):
    def __init__(self, nombre, email, codigo_postal):
        super().__init__(nombre, email)
        self.codigo_postal = codigo_postal

# Misma idea para admin.
class Admin(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)

    def is_admin(self):
        return True
