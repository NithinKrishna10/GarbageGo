# Generated by Django 4.2.1 on 2023-05-22 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_customer_name_remove_order_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pickup_time',
        ),
    ]
