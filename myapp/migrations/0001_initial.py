# Generated by Django 4.2.14 on 2024-07-18 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Complaint",
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
                ("product_name", models.CharField(max_length=255)),
                ("purchase_date", models.DateField()),
                ("complaint_details", models.TextField()),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
