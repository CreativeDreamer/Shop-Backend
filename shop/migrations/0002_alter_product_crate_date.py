# Generated by Django 4.0.2 on 2022-02-06 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='crate_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 2, 6, 11, 54, 2, 321415)),
        ),
    ]
