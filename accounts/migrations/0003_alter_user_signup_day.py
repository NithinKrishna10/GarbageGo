# Generated by Django 4.2.1 on 2023-06-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_admin_user_signup_day_user_signup_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signup_day',
            field=models.CharField(default=4, max_length=50),
        ),
    ]