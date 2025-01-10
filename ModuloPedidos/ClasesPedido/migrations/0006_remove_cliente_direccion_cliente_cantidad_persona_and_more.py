# Generated by Django 5.1.4 on 2025-01-09 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClasesPedido', '0005_rename_esta_cocinando_personalcocina_esta_cocinando_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='direccion',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cantidad_persona',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
        migrations.AddField(
            model_name='cliente',
            name='es_para_llevar',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='cliente',
            name='realizo_pedido',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
