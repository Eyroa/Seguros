# Generated by Django 4.1.7 on 2023-05-15 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_seguros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.CharField(max_length=16, verbose_name='CUIT/CUIL'),
        ),
    ]
