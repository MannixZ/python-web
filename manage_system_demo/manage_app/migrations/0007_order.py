# Generated by Django 4.1.7 on 2023-06-06 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manage_app", "0006_task"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("oid", models.CharField(max_length=64, verbose_name="订单号")),
                ("title", models.CharField(max_length=32, verbose_name="名称")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="价格"
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "已售"), (2, "未售")], default=1, verbose_name="状态"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manage_app.userinfo",
                        verbose_name="负责人",
                    ),
                ),
            ],
        ),
    ]