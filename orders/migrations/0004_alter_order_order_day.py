# Generated by Django 4.2.1 on 2023-06-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_order_day_order_order_month_order_order_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Order_day',
            field=models.IntegerField(default=4),
        ),
    ]
