# Generated by Django 4.2.11 on 2024-03-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignment", "0005_devicelog_device_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="devicelog",
            name="returned_condition",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]