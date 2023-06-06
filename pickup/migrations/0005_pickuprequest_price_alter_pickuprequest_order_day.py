# Generated by Django 4.2.1 on 2023-06-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickup', '0004_alter_pickuprequest_pickup_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickuprequest',
            name='price',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pickuprequest',
            name='Order_day',
            field=models.IntegerField(default=5),
        ),
    ]