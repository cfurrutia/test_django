from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CrearUsuarioForm, LoginForm, ImagenForm, ComentarioForm
from .models import Imagenes, Comentario, Categoria, Usuario
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)  
            user.save()
            Usuario.objects.create(user=user, nombre=user.username)
            return redirect('login')
    else:
        form = CrearUsuarioForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('imagenes')
            else:
                form.add_error(None, "Nombre de usuario o contraseña inválidos.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def obtener_imagenes(request):
    imagenes = Imagenes.objects.all().order_by('-fecha')
    return render(request, 'imagenes.html', {'imagenes': imagenes})

@login_required
def detalle_imagen(request, id):
    imagen = get_object_or_404(Imagenes, id=id)
    comentarios = Comentario.objects.filter(imagen=imagen)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.user = request.user
            comentario.imagen = imagen
            comentario.save()
            return redirect('detalle_imagen', id=id)
    else:
        form = ComentarioForm()
    return render(request, 'detalle_imagen.html', {'imagen': imagen, 'comentarios': comentarios, 'form': form})

@login_required
def agregar_imagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            imagen = form.save(commit=False)
            imagen.user = request.user.usuario
            imagen.save()
            return redirect('detalle_imagen', id=imagen.id)
    else:
        form = ImagenForm()
    return render(request, 'agregar_imagen.html', {'form': form})
