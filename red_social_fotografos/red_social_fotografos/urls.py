from django.contrib import admin
from django.urls import path
from redsocial.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('imagenes/', obtener_imagenes, name='imagenes'),
    path('imagen/<int:id>/', detalle_imagen, name='detalle_imagen'),
    path('agregar_imagen/', agregar_imagen, name='agregar_imagen'),
]
