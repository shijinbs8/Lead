# Generated by Django 4.2.2 on 2023-06-24 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Class",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Blub",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("token", models.TextField()),
                ("pin", models.CharField(max_length=10)),
                ("status", models.IntegerField()),
                (
                    "classname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="apps.class"
                    ),
                ),
            ],
        ),
    ]
