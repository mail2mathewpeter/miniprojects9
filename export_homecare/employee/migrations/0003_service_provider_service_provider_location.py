# Generated by Django 4.2.1 on 2024-07-31 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_service_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_provider',
            name='Service_Provider_location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
