# Generated by Django 4.2.1 on 2024-07-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Gender',
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
