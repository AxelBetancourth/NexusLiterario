from django.shortcuts import render, redirect
from .forms import FormularioLogin, FormularioAprobando
from .models import Users
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import check_password, make_password
import bcrypt
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def main(request):
    return render(request, 'index/main.html')

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
            
            # Verifica si el nombre de usuario ya existe
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
