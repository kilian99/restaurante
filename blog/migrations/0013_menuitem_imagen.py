# Generated by Django 4.2.16 on 2024-11-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_mesa_capacidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='menu/'),
        ),
    ]
