from django.shortcuts import render, redirect
from .forms import FormularioLogin, FormularioAprobando
from .models import Users
from administrator.models import Libros, Categorias, Categorias_Libros
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
import bcrypt


def main(request):
    categorias = Categorias.objects.all()
    libros_recientes = Libros.objects.order_by('-Fecha_Now')[:4]
    
    # Obtener categorías seleccionadas
    categorias_seleccionadas = request.GET.getlist('categoria')
    
    # Filtrar libros por categorías seleccionadas
    if categorias_seleccionadas:
        otros_libros = Libros.objects.filter(
            categorias_libros__Id_Categorias__Categorias__in=categorias_seleccionadas
        ).distinct().order_by('-Fecha_Now')
    else:
        otros_libros = Libros.objects.order_by('-Fecha_Now')[4:]
    
    paginator = Paginator(otros_libros, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'libros_recientes': libros_recientes,
        'page_obj': page_obj,
        'categorias': categorias,
        'categorias_seleccionadas': categorias_seleccionadas,
    }
    return render(request, 'index/main.html', context)

def main2(request):
    return render(request, 'index/main2.html')

def user(request):
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                return redirect(f"{request.path}?error=Las contraseñas no coinciden.")
            
            if Users.objects.filter(user_name=username).exists():
                return redirect(f"{request.path}?error=Este nombre de usuario ya está en uso.")
            
            hashed_password = make_password(password)
            
            try:
                Users.objects.create(
                    correo=email,
                    user_name=username,
                    password=hashed_password,
                    tipo='cliente'
                )
                return redirect(f"{request.path}?success=Registro exitoso. Puedes iniciar sesión.")
            except:
                return redirect(f"{request.path}?error=Error al crear el usuario.")
    else:
        form = FormularioLogin()

    return render(request, 'auth/reg_user.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = FormularioAprobando(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            try:
                user = Users.objects.get(user_name=username)
                if check_password(password, user.password):
                    request.session['user_id'] = user.Id_User
                    if user.tipo == 'administrador':
                        return redirect('admin')
                    else:
                        print('re redigira a cliente')
                        return redirect('main')
                else:
                    messages.error(request, 'Credenciales incorrectas.')
            except Users.DoesNotExist:
                messages.error(request, 'Credenciales incorrectas.')
    else:
        form = FormularioLogin()

    return render(request, 'auth/login.html', {'form': form})

def logout(request):
    return render(request, 'index/main.html')
