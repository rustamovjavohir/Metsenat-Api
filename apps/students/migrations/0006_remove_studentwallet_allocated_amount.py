# Generated by Django 4.1.3 on 2022-11-27 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0005_studentwallet_allocated_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentwallet",
            name="allocated_amount",
        ),
    ]
