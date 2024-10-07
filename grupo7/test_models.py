import unittest
from models import Usuario, Producto, Transaccion

class TestPonzi(unittest.TestCase):
    
    def test_agregar_referido(self):
        usuario = Usuario("Juan", "juan@test.com")
        referido = Usuario("Pedro", "pedro@test.com")
        usuario.agregar_referido(referido)
        self.assertIn(referido, usuario.referidos)
        self.assertEqual(usuario.balance, 100)

    def test_realizar_compra(self):
        usuario = Usuario("Juan", "juan@test.com")
        usuario.balance = 200
        producto = Producto("Producto 1", 150)
        transaccion = Transaccion(usuario, producto)
        self.assertTrue(transaccion.realizar_compra())
        self.assertEqual(usuario.balance, 50)

    def test_obtener_referidos(self):
        usuario = Usuario("Juan", "juan@test.com")
        referido = Usuario("Pedro", "pedro@test.com")
        usuario.agregar_referido(referido)
        self.assertEqual(len(usuario.referidos), 1)

    def test_historial_transacciones(self):
        usuario = Usuario("Juan", "juan@test.com")
        usuario.balance = 200
        producto = Producto("Producto 1", 150)
        transaccion = Transaccion(usuario, producto)
        transaccion.realizar_compra()
        self.assertIn(transaccion, Transaccion.historial)

if __name__ == '__main__':
    unittest.main()
