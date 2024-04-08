from django import forms
from .models import Reservation, Apartment, ApartmentImage


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ApartmentForm, self).__init__(*args, **kwargs)
        self.fields['deal_type'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['city'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['side'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['capacity'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['room'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['square'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['floor'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['total_floors'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['singlebeds'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['doublebeds'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['price'].widget.attrs.update({'class': 'form-control form-control-lg'})

class ApartmentImageForm(forms.ModelForm):
    class Meta:
        model = ApartmentImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['multiple'] = True
        self.fields['image'].widget.attrs.update({'class': 'form-control form-control-lg'})

class ApartmentAddForm(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = ['owner', 'status']

    def __init__(self, *args, **kwargs):
        super(ApartmentAddForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                # Если это чекбокс, обновляем класс атрибута для его виджета
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                # Для остальных полей, например, текстовых полей, используем form-control-lg
                field.widget.attrs.update({'class': 'form-control form-control-lg'})


class ApartmentFilterForm(forms.Form):
    ROOM_COUNT = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

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


    city_choice = forms.ChoiceField(required=False, label='Город')
    room_choice = forms.ChoiceField(choices=ROOM_COUNT, required=False, label='Комнат')
    price_choice = forms.ChoiceField(choices=PRICE_CHOICES, required=False, label='Цена')



class ApartmentBuyFilterForm(ApartmentFilterForm, forms.Form):

    FLOOR_CHOICES = (
        ('', 'Любой'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('6+', '6+'),

    )
    ROOM_CHOICES = (
        ('', 'Любое'),
        ('1', '1 комната'),
        ('2', '2 комнаты'),
        ('3', '3 комната'),
        ('4', '4 комнаты'),
        ('5', '5 комнат'),
        ('6', '6 комнат'),
        ('7', '7+ комнат'),

        # Другие варианты количества комнат
    )
    SQUARE_CHOICES = (
        ('', 'Любая'),
        ('50', 'До 50 кв.м'),
        ('100', 'До 100 кв.м'),
        ('100', 'Более 100 кв.м'),
    )

    floor_choice = forms.ChoiceField(choices=FLOOR_CHOICES, required=False, label='Этаж')
    room_choice = forms.ChoiceField(choices=ROOM_CHOICES, required=False, label='Комнат')
    square_choice = forms.ChoiceField(choices=SQUARE_CHOICES, required=False, label='Площадь')
    price_from = forms.FloatField(required=False, label='Цена от')
    price_to = forms.FloatField(required=False, label='Цена до')

    def __init__(self, *args, **kwargs):
        super(ApartmentBuyFilterForm, self).__init__(*args, **kwargs)
        self.fields['floor_choice'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['room_choice'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['square_choice'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['price_from'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['price_to'].widget.attrs.update({'class': 'form-control form-control-lg'})


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'surname', 'phone']
