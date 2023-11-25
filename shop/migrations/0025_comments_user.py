# Generated by Django 4.0.2 on 2022-04-01 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0011_remove_user_des_alter_user_address_and_more'),
        ('shop', '0024_alter_comments_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users_api.user'),
        ),
    ]