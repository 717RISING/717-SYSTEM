from django.http import HttpResponse
import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .captcha_generator import generate_captcha

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def contacto(request):
    return render(request, 'contacto.html')

def login(request):
    return render(request, 'login.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def legal(request):
    return render(request, 'legal.html')

def register(request):
    return render(request, 'register.html')

def perfil(request):
    return render(request, 'perfil.html')

def pedidos(request):
    return render(request, 'pedidos.html')

def favoritos(request):
    return render(request, 'favoritos.html')

def detalles(request):
    return render(request, 'detalles.html')

def editar_perfil(request):
    return render(request, 'editar_perfil.html')


def login_view(request):
    captcha_text, captcha_filename = generate_captcha()  # Generar un nuevo CAPTCHA

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_captcha = request.POST.get("captcha")  # CAPTCHA ingresado por el usuario
        correct_captcha = request.session.get("captcha_text")  # CAPTCHA correcto

        user = authenticate(request, username=username, password=password)

        if user is not None and user_captcha.upper() == correct_captcha:
            login(request, user)
            return redirect("home")  # Redirigir al usuario a la página principal
        else:
            error_message = "Usuario, contraseña o CAPTCHA incorrecto."

    else:
        error_message = None

    # Guardar el CAPTCHA en la sesión para compararlo después
    request.session["captcha_text"] = captcha_text

    return render(request, "login.html", {
        "error_message": error_message,
        "captcha_image": f"captchas/{captcha_filename}"
    })