from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index/main.html')

def user(request):
    return render(request, 'auth/reg_user.html')

def login(request):
    return render(request, 'auth/login.html')
