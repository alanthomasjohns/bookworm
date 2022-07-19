# Generated by Django 4.0.5 on 2022-07-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='New', max_length=20),
        ),
    ]
