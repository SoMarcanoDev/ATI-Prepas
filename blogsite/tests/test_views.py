from django.test import TestCase
from django.urls import reverse
from blogsite.models import UsuarioSimple, Blog

class VistasBlogsiteTests(TestCase):

    def setUp(self):
        """ Configuración inicial para las pruebas de vistas """
        self.usuario = UsuarioSimple.objects.create(
            nombre="Sofia",
            email="sofia@example.com"
        )
        self.blog = Blog.objects.create(
            titulo="Mi primer post de prueba",
            contenido="Este es el contenido detallado del post de prueba.",
            autor=self.usuario
        )

    def test_vista_lista_blogs(self):
        """ Prueba la vista que lista todos los blogs """
        response = self.client.get(reverse('lista_blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista.html')
        self.assertContains(response, "Mi primer post de prueba")

    def test_vista_detalle_blog_existente(self):
        """ Prueba la vista de detalle con un ID que sí existe """
        url = reverse('detalle_blog', args=[self.blog.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalle.html')
        self.assertContains(response, "Este es el contenido detallado del post de prueba.")
        self.assertContains(response, "Sofia")

    def test_vista_detalle_blog_no_existente(self):
        """ Prueba que la vista devuelva un error 404 si el blog no existe """
        url = reverse('detalle_blog', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)