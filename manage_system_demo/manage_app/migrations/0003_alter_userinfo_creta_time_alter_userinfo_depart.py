# Generated by Django 4.1.7 on 2023-05-22 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manage_app", "0002_alter_userinfo_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="creta_time",
            field=models.DateField(verbose_name="入职时间"),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="depart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="manage_app.department",
                verbose_name="部门",
            ),
        ),
    ]
