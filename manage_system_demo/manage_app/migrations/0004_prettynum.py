# Generated by Django 4.1.7 on 2023-05-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manage_app", "0003_alter_userinfo_creta_time_alter_userinfo_depart"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrettyNum",
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
                ("mobile", models.CharField(max_length=32, verbose_name="手机号")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, verbose_name="价值"
                    ),
                ),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(1, "Lv1"), (2, "Lv2"), (3, "Lv3"), (4, "Lv4")],
                        default=1,
                        verbose_name="等级",
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "占用"), (2, "未占用")], default=2, verbose_name="占用状态"
                    ),
                ),
            ],
        ),
    ]