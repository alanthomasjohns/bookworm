# Generated by Django 4.0.5 on 2022-07-27 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_order_product_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('New', 'New'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='New', max_length=20),
        ),
    ]
