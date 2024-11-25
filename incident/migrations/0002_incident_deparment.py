# Generated by Django 4.2.7 on 2023-12-04 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("department", "0001_initial"),
        ("incident", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="incident",
            name="deparment",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="department.deparment",
            ),
        ),
    ]