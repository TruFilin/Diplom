# Generated by Django 5.1.6 on 2025-02-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forklifts', '0002_create_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forklift',
            name='model',
            field=models.CharField(max_length=100),
        ),
    ]
