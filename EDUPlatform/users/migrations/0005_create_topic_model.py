# Generated by Django 4.1 on 2022-10-13 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_create_course_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
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
                ("topic_name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="")),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.course",
                    ),
                ),
            ],
            options={
                "verbose_name": "topic",
                "verbose_name_plural": "topics",
            },
        ),
    ]
