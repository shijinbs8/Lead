# Generated by Django 4.2.2 on 2023-06-24 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0002_remove_blub_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blub",
            name="token",
            field=models.CharField(max_length=100),
        ),
    ]
