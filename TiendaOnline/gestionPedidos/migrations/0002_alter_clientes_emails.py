# Generated by Django 4.1.5 on 2023-01-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='emails',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
