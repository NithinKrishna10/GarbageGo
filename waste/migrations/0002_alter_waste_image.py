# Generated by Django 4.2.1 on 2023-05-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waste',
            name='image',
            field=models.ImageField(blank=True, upload_to='waste_category'),
        ),
    ]
