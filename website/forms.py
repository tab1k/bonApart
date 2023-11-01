from django import forms


class ApartmentFilterForm(forms.Form):
    CLASS_CHOICES = [
        ('', 'Выберите класс'),
        ('comfort', 'Комфорт'),
        ('business', 'Бизнес'),
        ('premium', 'Премиум'),
    ]

    PRICE_CHOICES = [
        ('', 'Выберите цену'),
        ('1', 'от 10.000 тг'),
        ('2', '10.000 тг - 15.000 тг'),
        ('3', '15.000 тг - 20.000 тг'),
        ('4', '20.000 тг - 25.000 тг'),
        ('5', '20.000+ тг'),
    ]

    RATING_CHOICES = [
        ('', 'Выберите рейтинг'),
        ('1', '1 звезда'),
        ('2', '2 звезды'),
        ('3', '3 звезды'),
        ('4', '4 звезды'),
        ('5', '5 звезд'),
    ]

    ADDITIONAL_CHOICES = [
        ('wifi', 'Wi-Fi'),
        ('air_conditioning', 'Кондиционер'),
        ('parking', 'Платная парковка'),
        ('bath', 'Ванна'),
        ('orthopedic_mattress', 'Ортопедический матрац'),
        ('smart_tv', 'Smart TV'),
        ('hairdryer', 'Фен'),
        ('iron', 'Утюг'),
        ('washing_machine', 'Стиральная машина'),
        ('elevator', 'Лифт'),
    ]

    class_choice = forms.ChoiceField(choices=CLASS_CHOICES, required=False, label='Класс квартир')
    price_choice = forms.ChoiceField(choices=PRICE_CHOICES, required=False, label='Цена')
    rating_choice = forms.ChoiceField(choices=RATING_CHOICES, required=False, label='Рейтинг')
    additional_choice = forms.MultipleChoiceField(choices=ADDITIONAL_CHOICES, required=False,
                                                  widget=forms.CheckboxSelectMultiple, label='Дополнительно')


class CarFilterForm(forms.Form):

    CLASS_CHOICES = (
        ('comfort', 'Комфорт'),
        ('business', 'Бизнес'),
    )

    class_choice = forms.ChoiceField(choices=CLASS_CHOICES,
                                     required=False,
                                     label='Класс машины')




from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'surname', 'phone']
