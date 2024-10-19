# Generated by Django 4.2.1 on 2024-07-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Gender',
            new_name='status',
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]