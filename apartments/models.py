from django.db import models

# Create your models here.

class Apartment(models.Model):

    DEAL_CHOICES = (
        ('daily_rent', 'Аренда по суточно'),
        ('monthly_rent', 'Аренда помесячно'),
        ('sale', 'Продажа'),
    )

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

    deal_type = models.CharField(max_length=20, choices=DEAL_CHOICES, default='daily_rent', verbose_name='Тип сделки')
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

    image6 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    image7 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    image8 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    image9 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    image10 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)

    image11 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)
    image12 = models.ImageField(upload_to='apartment_images/', blank=True, null=True)

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
    photo = models.ImageField(upload_to='geo_images', null=True, blank=True)
    link = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Геопозиция дома'
        verbose_name_plural = 'Геопозиции домов'


class Reservation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.name} | {self.phone}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'