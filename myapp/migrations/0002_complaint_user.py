# Generated by Django 4.2.14 on 2024-07-19 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaint",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="complaints",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
