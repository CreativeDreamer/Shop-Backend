# Generated by Django 4.0.2 on 2022-02-12 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_image_imageurl_alter_image_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='imageurl',
            new_name='imageUrl',
        ),
    ]