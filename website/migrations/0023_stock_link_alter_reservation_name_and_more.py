# Generated by Django 4.2.6 on 2023-11-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0022_stock_end_date_stock_start_date_alter_stock_valid"),
    ]

    operations = [
        migrations.AddField(
            model_name="stock",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="phone",
            field=models.CharField(max_length=20, verbose_name="Номер телефона"),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="surname",
            field=models.CharField(max_length=255, verbose_name="Фамилия"),
        ),
        migrations.AlterField(
            model_name="stock",
            name="about",
            field=models.TextField(blank=True, null=True, verbose_name="О акции"),
        ),
        migrations.AlterField(
            model_name="stock",
            name="end_date",
            field=models.DateField(blank=True, null=True, verbose_name="Конец акции"),
        ),
        migrations.AlterField(
            model_name="stock",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="stock_images",
                verbose_name="Задний фон",
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="start_date",
            field=models.DateField(blank=True, null=True, verbose_name="Начало акции"),
        ),
        migrations.AlterField(
            model_name="stock",
            name="stock",
            field=models.CharField(max_length=255, verbose_name="Акция"),
        ),
        migrations.AlterField(
            model_name="stock",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Хэштег"),
        ),
        migrations.AlterField(
            model_name="stock",
            name="valid",
            field=models.BooleanField(
                blank=True, default=True, null=True, verbose_name="Действует акция?"
            ),
        ),
    ]
