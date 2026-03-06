from django.test import TestCase

class MiPrueba(TestCase):
    def test_suma(self):
        resultado = 2 + 2
        self.assertEqual(resultado, 4)