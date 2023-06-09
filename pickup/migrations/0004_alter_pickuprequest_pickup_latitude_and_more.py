# Generated by Django 4.2.1 on 2023-06-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickup', '0003_remove_pickuprequest_contact_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickuprequest',
            name='pickup_latitude',
            field=models.DecimalField(blank=True, decimal_places=30, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='pickuprequest',
            name='pickup_longitude',
            field=models.DecimalField(blank=True, decimal_places=30, max_digits=50, null=True),
        ),
    ]
