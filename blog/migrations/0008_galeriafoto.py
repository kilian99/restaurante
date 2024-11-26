# Generated by Django 4.2.16 on 2024-11-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_reserva_num_personas'),
    ]

    operations = [
        migrations.CreateModel(
            name='GaleriaFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100)),
                ('imagen', models.ImageField(upload_to='gallery/')),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
    ]
