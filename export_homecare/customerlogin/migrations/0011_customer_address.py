# Generated by Django 4.2.1 on 2024-08-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerlogin', '0010_booking_amount_booking_paymentstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]