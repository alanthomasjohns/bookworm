# Generated by Django 4.0.5 on 2022-07-27 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_bestsellers'),
        ('orders', '0022_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
