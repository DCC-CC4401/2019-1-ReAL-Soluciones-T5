# Generated by Django 2.2.1 on 2019-05-10 05:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190510_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='fecha_fin',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 5, 10, 5, 42, 37, 283037, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 5, 10, 5, 42, 37, 283017, tzinfo=utc)),
        ),
    ]
