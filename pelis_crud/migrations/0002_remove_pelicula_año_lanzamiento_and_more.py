# Generated by Django 4.2.6 on 2023-10-13 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelis_crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='año_lanzamiento',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='genero',
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
