# Generated by Django 4.1.1 on 2022-10-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testing_system", "0009_create_attempt_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.RemoveField(
            model_name="topic",
            name="image",
        ),
        migrations.AddField(
            model_name="topic",
            name="image",
            field=models.ManyToManyField(blank=True, null=True, to="testing_system.image"),
        ),
    ]
