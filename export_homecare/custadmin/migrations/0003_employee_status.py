# Generated by Django 4.2.1 on 2024-07-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custadmin', '0002_remove_employee_gender_employee_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
