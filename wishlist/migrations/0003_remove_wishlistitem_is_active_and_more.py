# Generated by Django 4.0.5 on 2022-07-15 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_wishlistitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='wishlist',
        ),
    ]
