# Generated by Django 2.2.13 on 2022-06-26 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220625_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='api.Sucursal'),
        ),
    ]
