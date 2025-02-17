# Generated by Django 5.1.6 on 2025-02-16 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forklifts', '0006_remove_technicalservice_service_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='service_company',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='downtime',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='failure_node',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='recovery_method',
            field=models.CharField(max_length=100),
        ),
    ]
