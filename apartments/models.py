import os
from datetime import timezone, datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from PIL import Image
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta


class Apartment(models.Model):

    DEAL_CHOICES = (
        ('daily_rent', 'Аренда по суточно'),
        ('monthly_rent', 'Аренда помесячно'),
        ('sale', 'Продажа'),
    )

    ROOM_COUNT = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    STATUS_CHOICES = (
        ('pending', 'На рассмотрении'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
        # Добавьте другие статусы, если нужно
    )

    approval_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата одобрения')
    expiry_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата истечения срока годности')
    archived = models.BooleanField(default=False, verbose_name='В архиве')

    deal_type = models.CharField(max_length=20, choices=DEAL_CHOICES, default='daily_rent', verbose_name='Тип сделки')
    city = models.ForeignKey('City', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Города')
    name = models.CharField(max_length=355, verbose_name = 'Название ЖК')
    address = models.CharField(max_length=355, verbose_name = 'Адрес ЖК', blank=True, null=True)
    description = models.TextField(verbose_name='Подробнее')
    side = models.CharField(max_length=255, verbose_name='Район', blank=True, null=True)

    capacity = models.PositiveIntegerField(default=2, verbose_name='Вместимость')
    room = models.CharField(choices=ROOM_COUNT, max_length=255 ,verbose_name='Комнат')
    square = models.PositiveIntegerField(default=37, verbose_name='Площадь')
    floor = models.PositiveIntegerField(default=5, verbose_name='Этаж')
    total_floors = models.PositiveSmallIntegerField(verbose_name='Кол-во этажей')

    singlebeds = models.PositiveSmallIntegerField(default=1, verbose_name='Односпальных мест')
    doublebeds = models.PositiveSmallIntegerField(default=1, verbose_name='Двухспальных мест')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    video = models.URLField(blank=True, null=True, verbose_name='Видео-ролик')

    wifi = models.BooleanField(default=False, verbose_name='Wi-Fi')
    elevator = models.BooleanField(default=True, verbose_name='Лифт')
    air_conditioning = models.BooleanField(default=False, verbose_name='Кондиционер')
    parking = models.BooleanField(default=False, verbose_name='Платный паркинг')
    bath = models.BooleanField(default=False, verbose_name='Ванна')
    orthopedic_mattress = models.BooleanField(default=False, verbose_name='Ортопедический матрац')
    smart_tv = models.BooleanField(default=False, verbose_name='Smart TV')
    hairdryer = models.BooleanField(default=False, verbose_name='Фен')
    iron = models.BooleanField(default=False, verbose_name='Утюг')
    washing_machine = models.BooleanField(default=False, verbose_name='Стиральная машинка')

    fridge = models.BooleanField(default=False, verbose_name='Холодильник')
    electric_kettle = models.BooleanField(default=False, verbose_name='Электрический чайник')
    plate = models.BooleanField(default=False, verbose_name='Плита')
    mini_bar = models.BooleanField(default=False, verbose_name='Мини Бар')
    hygiene = models.BooleanField(default=False, verbose_name='Гигиенические принадлежности')
    dishes = models.BooleanField(default=False, verbose_name='Посуда')
    shower = models.BooleanField(default=False, verbose_name='Душ')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_apartments', blank=True, null=True)

    def upload_to(self, filename):
        # Генерируем уникальное имя для файла
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename_base, filename_ext = os.path.splitext(filename)
        filename = f"{timestamp}-{filename_base}{filename_ext}"

        # Определяем путь для сохранения файла
        return f"apartment_images/{filename}"

    def save(self, *args, **kwargs):
        if self.status == 'approved' and not self.approval_date:
            # Если квартира одобрена и у нее нет даты одобрения, устанавливаем текущую дату
            self.approval_date = timezone.now()

            # Устанавливаем дату истечения срока годности на 30 дней вперед от даты одобрения
            self.expiry_date = self.approval_date + timezone.timedelta(days=30)

        super().save(*args, **kwargs)

    def is_expired(self):
        # Проверяем, истек ли срок годности квартиры
        return self.expiry_date and self.expiry_date < timezone.now()

    def get_image_urls(self):
        return [image.image.url for image in self.images.all()]

    def archive_if_expired(self):
        # Помечаем квартиру как архивированную, если она просрочена
        if self.is_expired():
            self.archived = True
            self.save()

    def get_deal_type(self):
        return self.get_deal_type_display()

    def get_archive_bool(self):
        return "Да" if self.archived else "Нет"

    def get_owner_phone(self):
        return self.get_owner_phone()

    def get_status_type(self):
        return self.get_status_display()

    def is_available(self):
        today = timezone.now().date()
        # Проверяем, есть ли активные бронирования на сегодняшний день или будущие даты
        return not self.bookings.filter(end_date__gte=today).exists()

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='apartment_images/')

    def __str__(self):
        return f'Image for {self.apartment.name}'

    class Meta:
        verbose_name = 'Фото квартиры'
        verbose_name_plural = 'Фото квартир'


class Booking(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.apartment.name} | C {self.start_date} - До {self.end_date}'

    class Meta:
        verbose_name = 'Бронирование квартиры'
        verbose_name_plural = 'Бронирование квартиры'


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


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
