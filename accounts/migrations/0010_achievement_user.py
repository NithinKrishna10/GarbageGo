# Generated by Django 4.2.1 on 2023-06-08 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_achievement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
    ]