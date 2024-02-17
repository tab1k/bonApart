from django.db import models


class Car(models.Model):

    CLASS_CHOICES = (
        ('comfort', 'Комфорт'),
        ('business', 'Бизнес'),
    )

    EQUIPMENT_CHOICES = (
        ('minimal', 'Минимальная'),
        ('average', 'Средняя'),
        ('full', 'Полная'),
    )

    BODY_CHOICES = (
        ('sedan', 'Седан'),
        ('universal', 'Универсал'),
        ('hatchback', 'Хэтчбек'),
        ('crossover', 'Кроссовер'),
        ('jeep', 'Внедорожник'),
        ('limousine', 'Лимузин'),
    )

    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    image = models.ImageField(upload_to='images/', verbose_name='Фотография')
    level = models.CharField(max_length=10, choices=CLASS_CHOICES, verbose_name='Класс машины', blank=True, null=True)
    equipment = models.CharField(max_length=15, choices=EQUIPMENT_CHOICES, verbose_name='Комплектация')
    volume = models.FloatField(verbose_name='Объем')
    capacity = models.SmallIntegerField(verbose_name='Вместительность', blank=True, null=True)
    body = models.CharField(max_length=15, choices=BODY_CHOICES, verbose_name='Кузов', blank=True, null=True)
    day = models.SmallIntegerField(verbose_name='Время')
    price = models.PositiveIntegerField(verbose_name='Цена')

    def __str__(self):
        return f'{self.brand} {self.model}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'



class Stock(models.Model):
    title = models.CharField(max_length=255, verbose_name='Хэштег')
    stock = models.CharField(max_length=255, verbose_name='Акция')
    about = models.TextField(blank=True, null=True, verbose_name='О акции')
    photo = models.ImageField(upload_to='stock_images', blank=True, null=True, verbose_name='Задний фон')
    start_date = models.DateField(blank=True, null=True, verbose_name='Начало акции')
    end_date = models.DateField(blank=True, null=True, verbose_name='Конец акции')
    link = models.URLField(blank=True, null=True)
    valid = models.BooleanField(default=True, blank=True, null=True, verbose_name='Действует акция?')

    def str(self):
        return self.stock

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

