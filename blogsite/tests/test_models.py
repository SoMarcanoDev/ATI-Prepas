from django.test import TestCase
from blogsite.models import UsuarioSimple, Blog

class MiPrueba(TestCase):
    def test_suma(self):
        resultado = 2 + 2
        self.assertEqual(resultado, 4)
 

# Modelos Blog
class ModelosBlogsiteTests(TestCase):

    def setUp(self):
        """ Configuración inicial para las pruebas de modelos """
        self.usuario = UsuarioSimple.objects.create(
            nombre="Sofia",
            email="sofia@example.com"
        )
        self.blog = Blog.objects.create(
            titulo="Mi primer post de prueba",
            contenido="Este es el contenido detallado del post de prueba.",
            autor=self.usuario
        )

    def test_creacion_usuario(self):
        """ Verifica que el usuario se guarde correctamente y su representación __str__ """
        usuario = UsuarioSimple.objects.get(email="sofia@example.com")
        self.assertEqual(usuario.nombre, "Sofia")
        self.assertEqual(str(usuario), "Sofia")

    def test_creacion_blog(self):
        """ Verifica que el blog se guarde con los datos correctos y su __str__ """
        blog = Blog.objects.get(titulo="Mi primer post de prueba")
        self.assertEqual(blog.contenido, "Este es el contenido detallado del post de prueba.")
        self.assertEqual(blog.autor, self.usuario)
        self.assertEqual(str(blog), "Mi primer post de prueba")
