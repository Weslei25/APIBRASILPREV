# Generated by Django 4.1.5 on 2023-01-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_clientemodel_cpf_alter_clientemodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientemodel',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]
