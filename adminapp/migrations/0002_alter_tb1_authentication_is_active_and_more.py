# Generated by Django 4.2.14 on 2024-07-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tb1_authentication",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="tb1_authentication",
            name="password",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="tb1_authentication",
            name="username",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
