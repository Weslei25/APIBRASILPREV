# Generated by Django 4.1.5 on 2023-01-15 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_clientemodel_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientemodel',
            name='rendaMensal',
        ),
    ]
