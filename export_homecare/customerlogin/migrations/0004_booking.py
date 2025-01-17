# Generated by Django 4.2.1 on 2024-08-03 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_service_provider_service_provider_location'),
        ('customerlogin', '0003_alter_customer_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField()),
                ('service_start_date', models.DateField()),
                ('service_end_date', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.service_provider')),
            ],
        ),
    ]
