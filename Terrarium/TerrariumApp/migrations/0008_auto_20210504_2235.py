# Generated by Django 3.2.1 on 2021-05-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TerrariumApp', '0007_rename_humidite_terrarium_humidity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terrarium',
            name='humidity',
        ),
        migrations.AddField(
            model_name='terrarium',
            name='humidite',
            field=models.DecimalField(decimal_places=2, default=65, max_digits=4),
            preserve_default=False,
        ),
    ]
