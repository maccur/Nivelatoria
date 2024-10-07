from flask import Flask, render_template, request
from models import db, UsuarioModel, ProductoModel, TransaccionModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/comprar', methods=['POST'])

def comprar():
    usuario_id = request.form['usuario_id']
    producto_id = request.form['producto_id']
    usuario = UsuarioModel.query.get(usuario_id)
    producto = ProductoModel.query.get(producto_id)

    if not usuario:
        return "Usuario no encontrado", 404
    
    if not producto:
        return "Producto no encontrado", 404
    
    transaccion = TransaccionModel(usuario=usuario, producto=producto)
    
    if transaccion.usuario.balance >= transaccion.producto.precio:
        transaccion.usuario.balance -= transaccion.producto.precio
        db.session.add(transaccion)
        db.session.commit()
        return "Compra realizada con éxito"
    return "No tiene saldo suficiente"

@app.route('/usuarios')
def listar_usuarios():
    usuarios = UsuarioModel.query.all()
    usuarios_info = [{"nombre": u.nombre, "balance": u.balance} for u in usuarios]
    return render_template('usuarios.html', usuarios=usuarios_info)

if __name__ == '__main__':
    app.run(debug=True)