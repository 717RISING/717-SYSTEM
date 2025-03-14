# Generated by Django 4.0.6 on 2025-02-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevenoneseven', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='cantidad',
            field=models.IntegerField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario',
            name='detalles',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario',
            name='valor_compra',
            field=models.IntegerField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario',
            name='valor_venta',
            field=models.IntegerField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='peso',
            field=models.IntegerField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
