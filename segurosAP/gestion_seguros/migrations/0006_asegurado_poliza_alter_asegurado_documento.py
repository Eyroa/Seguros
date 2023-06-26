# Generated by Django 4.2.1 on 2023-06-25 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_seguros', '0005_rename_aseugrado_certificado_asegurado'),
    ]

    operations = [
        migrations.AddField(
            model_name='asegurado',
            name='poliza',
            field=models.ManyToManyField(related_name='asegurados', to='gestion_seguros.poliza'),
        ),
        migrations.AlterField(
            model_name='asegurado',
            name='documento',
            field=models.IntegerField(verbose_name='Documento'),
        ),
    ]