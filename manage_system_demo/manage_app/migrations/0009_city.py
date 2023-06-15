# Generated by Django 4.1.7 on 2023-06-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manage_app", "0008_boss"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=32, verbose_name="名称")),
                ("count", models.IntegerField(verbose_name="人口")),
                (
                    "img",
                    models.FileField(
                        max_length=64, upload_to="city/", verbose_name="oLog"
                    ),
                ),
            ],
        ),
    ]
