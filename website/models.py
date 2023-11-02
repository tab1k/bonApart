from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Apartment(models.Model):

    CLASS_CHOICES = (
        ('lux', 'Люкс'),
        ('business', 'Бизнес'),
        ('prestige', 'Престиж'),
    )

    RATING_CHOICES = (
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    )

    SIDES_CHOICES = (
        ('ala', 'Алматинский'),
        ('bai', 'Байконурский'),
        ('esil', 'Есильский'),
        ('nurin', 'Нуринский'),
        ('sary', 'Сарыаркинский'),
    )


    name = models.CharField(max_length=355, verbose_name = 'Название ЖК')
    address = models.CharField(max_length=355, verbose_name = 'Адрес ЖК', blank=True, null=True)
    description = models.TextField(verbose_name='Подробнее')
    side = models.CharField(max_length=10, choices=SIDES_CHOICES, verbose_name='Район', blank=True, null=True)
    level = models.CharField(max_length=10, choices=CLASS_CHOICES, verbose_name='Класс квартиры', blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    capacity = models.PositiveIntegerField(default=2, verbose_name='Вместимость')
    room = models.PositiveIntegerField(default=1, verbose_name='Комнат')
    square = models.PositiveIntegerField(default=37, verbose_name='Площадь')
    floor = models.PositiveIntegerField(default=5, verbose_name='Этаж')
    total_floors = models.PositiveSmallIntegerField(verbose_name='Кол-во этажей')
    elevator = models.BooleanField(default=True, verbose_name='Лифт')
    singlebeds = models.PositiveSmallIntegerField(default=1, verbose_name='Односпальных мест')
    doublebeds = models.PositiveSmallIntegerField(default=1, verbose_name='Двухспальных мест')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image1 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    wifi = models.BooleanField(default=False, verbose_name='Wi-Fi')
    air_conditioning = models.BooleanField(default=False, verbose_name='Кондиционер')
    parking = models.BooleanField(default=False, verbose_name='Платный паркинг')
    bath = models.BooleanField(default=False, verbose_name='Ванна')
    orthopedic_mattress = models.BooleanField(default=False, verbose_name='Ортопедический матрац')
    smart_tv = models.BooleanField(default=False, verbose_name='Smart TV')
    hairdryer = models.BooleanField(default=False, verbose_name='Фен')
    iron = models.BooleanField(default=False, verbose_name='Утюг')
    washing_machine = models.BooleanField(default=False, verbose_name='Стиральная машинка')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class Discount(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ЖК')
    discount_count = models.IntegerField(null=True, blank=True, verbose_name='Скидка')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'




class GeoPosition(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ЖК')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')

    class Meta:
        verbose_name = 'Геопозиция дома'
        verbose_name_plural = 'Геопозиции домов'


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



class Reservation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.name} | {self.phone}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Stock(models.Model):
    title = models.CharField(max_length=255, verbose_name='Хэштег')
    stock = models.CharField(max_length=255, verbose_name='Акция')
    about = models.TextField(blank=True, null=True, verbose_name='О акции')
    photo = models.ImageField(upload_to='stock_images', blank=True, null=True, verbose_name='Задний фон')
    start_date = models.DateField(blank=True, null=True, verbose_name='Начало акции')  # Дата начала акции
    end_date = models.DateField(blank=True, null=True, verbose_name='Конец акции')  # Дата окончания акции
    valid = models.BooleanField(default=True, blank=True, null=True, verbose_name='Действует акция?')

    def str(self):
        return self.stock

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

