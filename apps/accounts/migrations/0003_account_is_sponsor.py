# Generated by Django 4.1.3 on 2022-11-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_account_role_alter_account_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="is_sponsor",
            field=models.BooleanField(default=False, verbose_name="Xomiy"),
        ),
    ]