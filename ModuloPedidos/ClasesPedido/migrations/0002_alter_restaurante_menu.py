# Generated by Django 5.1.4 on 2024-12-22 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClasesPedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='menu',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClasesPedido.menu'),
        ),
    ]