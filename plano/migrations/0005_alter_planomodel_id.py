# Generated by Django 4.1.5 on 2023-01-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plano', '0004_alter_planomodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planomodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
