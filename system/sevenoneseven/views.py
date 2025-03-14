from django.http import HttpResponse
from django.shortcuts import render

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