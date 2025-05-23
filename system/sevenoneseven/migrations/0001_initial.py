# Generated by Django 4.0.6 on 2025-02-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('medida', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('genero', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=500)),
                ('tipo', models.IntegerField(choices=[(1, 'Camiseta'), (2, 'Pantalon'), (3, 'Gorra'), (4, 'Accesorio')], default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_1', models.CharField(max_length=100)),
                ('nombre_2', models.CharField(max_length=100)),
                ('apellido_1', models.CharField(max_length=100)),
                ('apellido_2', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=254)),
                ('correo', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=254)),
                ('genero', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino'), (3, 'Otro')], default=3)),
                ('rol', models.IntegerField(choices=[(1, 'Admin'), (2, 'Empleado'), (3, 'cliente')], default=3)),
            ],
        ),
    ]
