# Generated by Django 4.2.16 on 2024-11-25 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_galeriafoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesa',
            name='capacidad',
        ),
    ]
