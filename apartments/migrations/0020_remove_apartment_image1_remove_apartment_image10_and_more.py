# Generated by Django 4.2.7 on 2024-04-07 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apartments", "0019_apartment_archived"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="apartment",
            name="image1",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image10",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image11",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image12",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image2",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image3",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image4",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image5",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image6",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image7",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image8",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="image9",
        ),
        migrations.CreateModel(
            name="ApartmentImage",
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
                ("image", models.ImageField(upload_to="apartment_images/")),
                (
                    "apartment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="apartments.apartment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото квартиры",
                "verbose_name_plural": "Фото квартир",
            },
        ),
    ]
