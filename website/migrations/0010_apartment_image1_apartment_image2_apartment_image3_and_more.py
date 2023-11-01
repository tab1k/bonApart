# Generated by Django 4.2.6 on 2023-10-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0009_car_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="apartment",
            name="image1",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image2",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image3",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image4",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="image5",
            field=models.ImageField(
                blank=True, null=True, upload_to="apartment_images/"
            ),
        ),
        migrations.DeleteModel(
            name="ApartmentImage",
        ),
    ]
