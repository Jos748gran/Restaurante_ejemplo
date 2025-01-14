# Generated by Django 5.1.4 on 2024-12-23 03:24

import ClasesPedido.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClasesPedido', '0003_alter_restaurante_registro_historico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='item_pedido_list',
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item_pedido_list', to='ClasesPedido.pedido'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='ClasesPedido.cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrohistorico',
            name='pedidos',
            field=models.ManyToManyField(blank=True, editable=False, to='ClasesPedido.pedido'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='historial',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='ClasesPedido.historial'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='mesa',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClasesPedido.mesa'),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='disponible',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='mesero',
            name='identificacion',
            field=models.CharField(editable=False, max_length=7, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('EN_PREPARACION', 'en_preparacion'), ('PAGADO', 'pagado'), ('PENDIENTE', 'pendiente'), ('PREPARADO', 'preparado'), ('SERVIDO', 'servido'), ('RESERVADO', 'reservado')], default=ClasesPedido.models.Estado['pendiente'], max_length=50),
        ),
        migrations.AlterField(
            model_name='personalcocina',
            name='identificacion',
            field=models.CharField(editable=False, max_length=7, null=True, unique=True),
        ),
    ]
