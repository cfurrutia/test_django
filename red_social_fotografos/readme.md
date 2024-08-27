# Red Social de Fotografía

Descripción
--
La página web es una red social de fotografía que permite a los usuarios ver imágenes y participar en los comentarios.La aplicación está desarrollada con Django y proporciona funcionalidades de autenticación, gestión de imágenes y comentarios.

Características
--
Registro y autenticación de usuarios.
Gestión de perfiles de usuario.
Subida, edición y eliminación de imágenes.
Visualización de imágenes y detalles.
Sistema de comentarios para las imágenes.
Interfaz adaptable y responsiva.

Tecnologías
--
Django 
Python
Bootstrap 5
HTML5
CSS3

Instalacion básica
--
python -m venv vpprueba

call vprueba\Scripts\activate    (cmd) 

django-admin startproject red_social_fotografos

cd red_social_fotografos

pip install -r requirements.txt


en setting.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "red_social_fotografos",
        "USER": "postgres",
        "PASSWORD": "Admin1234",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

python manage.py runserver
python manage.py migrate

#respalda todos los modelos de la aplicacion
python -Xutf8 manage.py dumpdata redsocial > red_social_fotografos.json
