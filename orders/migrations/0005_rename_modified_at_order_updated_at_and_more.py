# Generated by Django 4.0.5 on 2022-07-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Accepted', 'Accepted')], default='New', max_length=20),
        ),
    ]
