from django.contrib import admin
from .models import Usuario, Imagenes, Categoria, Comentario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Imagenes)
admin.site.register(Categoria)
admin.site.register(Comentario)