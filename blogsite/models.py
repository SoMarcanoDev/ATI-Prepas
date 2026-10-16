from django.db import models

# Create your models here.
class UsuarioSimple(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(UsuarioSimple, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.titulo