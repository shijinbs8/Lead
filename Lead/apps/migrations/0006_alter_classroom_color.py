# Generated by Django 4.2.2 on 2023-06-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0005_classroom_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classroom",
            name="color",
            field=models.CharField(max_length=100),
        ),
    ]
