# Generated by Django 4.1.3 on 2022-11-25 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="studentwallet",
            options={"verbose_name": "Student", "verbose_name_plural": "Students"},
        ),
    ]
