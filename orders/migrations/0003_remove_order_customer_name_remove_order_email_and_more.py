# Generated by Django 4.2.1 on 2023-05-22 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_address_name'),
        ('orders', '0002_alter_order_waste_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
    ]
