# Generated by Django 4.0.2 on 2022-02-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0009_alter_user_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='des',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
