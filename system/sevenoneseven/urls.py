from django.urls import path
from. import views
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("productos/", views.productos, name="productos"),
    path("contacto/", views.contacto, name="contacto"),
    path("login/", views.login, name="login"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("legal/", views.legal, name="legal"),
    path("register/", views.register, name="register"),
    path("perfil/", views.perfil, name="perfil"),
    path("pedidos/", views.pedidos, name="pedidos"),
    path("favoritos/", views.favoritos, name="favoritos"),
    path("detalles/", views.detalles, name="detalles"),
    path("editar-perfil/", views.editar_perfil, name= "editar_perfil")    
]