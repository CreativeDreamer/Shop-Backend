# Generated by Django 4.0.2 on 2022-04-29 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0058_alter_comments_product_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
