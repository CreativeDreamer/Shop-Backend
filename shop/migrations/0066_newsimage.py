# Generated by Django 4.0.2 on 2022-07-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0065_alter_order_state_alter_orderitem_imageurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imageUrl', models.ImageField(blank=True, null=True, upload_to='news_images/')),
            ],
        ),
    ]
