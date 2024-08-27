from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    TIPO_USUARIO = (
        ('administrador', 'Administrador'),
        ('fotografo', 'Fotógrafo'),
    )
    tipo_usuario = models.CharField(max_length=30, choices=TIPO_USUARIO, default='fotografo')

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Imagenes(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    url = models.URLField()
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario
