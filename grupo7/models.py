class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.referidos = []
        self.balance = 0

    def agregar_referido(self, referido):
        self.referidos.append(referido)
        self.balance += 100

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Transaccion:
    def __init__(self, usuario, producto):
        self.usuario = usuario
        self.producto = producto
        self.realizar_compra()

    def realizar_compra(self):
        if self.usuario.balance >= self.producto.precio:
            self.usuario.balance -= self.producto.precio
            return True
        return False