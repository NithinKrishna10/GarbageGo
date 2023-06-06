# Generated by Django 4.2.1 on 2023-06-04 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_signup_day'),
        ('pickup', '0002_item_invoice_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickuprequest',
            name='contact_person',
        ),
        migrations.RemoveField(
            model_name='pickuprequest',
            name='pickup_time',
        ),
        migrations.RemoveField(
            model_name='pickuprequest',
            name='quantity',
        ),
        migrations.AddField(
            model_name='pickuprequest',
            name='Order_day',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='pickuprequest',
            name='Order_month',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='pickuprequest',
            name='Order_year',
            field=models.IntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='pickuprequest',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
        migrations.AlterField(
            model_name='pickuprequest',
            name='pickup_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.address'),
        ),
        migrations.AlterField(
            model_name='pickuprequest',
            name='pickup_latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='pickuprequest',
            name='pickup_longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=50, null=True),
        ),
    ]
