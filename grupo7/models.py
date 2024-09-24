from flask_sqlalchemy import SQLAlchemy

#Clases

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
    

#SQL

db = SQLAlchemy()

class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

class ProductoModel(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)

class TransaccionModel(db.Model):
    __tablename__ = 'transacciones'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    usuario = db.relationship('UsuarioModel', backref='transacciones')
    producto = db.relationship('ProductoModel', backref='transacciones')


#Base de datos
def init_db():
    db.create_all()
    usuario = UsuarioModel(nombre="Juan", email="juan@test.com", balance=500)
    producto = ProductoModel(nombre="Producto 1", precio=150)
    db.session.add(usuario)
    db.session.add(producto)
    db.session.commit()