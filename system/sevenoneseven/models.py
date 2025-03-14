from django.db import models

# Create your models here.
class Usuario(models.Model):
    cedula = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=254)
    correo = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    fecha_nac = models.DateField(help_text="DD-MM-AAAA")

    ROLES =(
        (1, 'Admin'),
        (2, 'Empleado'),
        (3, 'Cliente'),
    )
    GENERO =(
        (1, 'Masculino'),
        (2, 'Femenino'),
        (3, 'Otro')
    )
    genero = models.IntegerField(choices=GENERO, default = 3)
    rol = models.IntegerField(choices=ROLES, default=3)
    
    def __str__(self):
        return f"{self.nombre}:{self.apellido}:{self.rol}:{self.correo}"
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    medida = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    descripcion = models.CharField(max_length=500)
    cantidad = models.IntegerField()
    peso = models.CharField(max_length=100)
    foto = models.CharField(max_length=100)
    TIPO =(
        (1, 'Camiseta'),
        (2, 'Pantalon'),
        (3, 'Gorra'),
        (4, 'Accesorio'),
        (5, 'Polo'),
    )
    tipo = models.IntegerField(choices=TIPO, default = 1)
    
    GENERO =(
        (1, 'Masculino'),
        (2, 'Femenino'),
    )
    gen = models.IntegerField(choices=GENERO, default = 1)
    
    def __str__(self):
        return f"{self.nombre}:{self.precio}:{self.descripcion}:"
    
    
class Factura(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name="fk1_factura_cliente")
    empleado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name="fk1_factura_empleado")
    precio = models.IntegerField()
    total = models.IntegerField()
    fecha = models.DateTimeField(help_text="AAAA-MM-DD")
    MEDIOPAGO =(
        (1, 'PSE'),
        (2, 'Tarjeta Credito'),
        (3, 'Tarjeta Debito'),
        (4, 'Efecty'),
    )
    medioPago = models.IntegerField(choices=MEDIOPAGO, default = 1)

class DetalleCompras(models.Model):
    precioProducto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    
