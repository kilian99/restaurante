# Generated by Django 4.2.16 on 2024-11-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_mesa_capacidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
    ]
