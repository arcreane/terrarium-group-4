# Generated by Django 3.2.1 on 2021-05-04 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TerrariumApp', '0006_alter_terrarium_humidite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='terrarium',
            old_name='humidite',
            new_name='humidity',
        ),
    ]