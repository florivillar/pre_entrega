# Generated by Django 4.2.6 on 2023-11-13 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comunidad_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunidad',
            name='miembros',
        ),
    ]
