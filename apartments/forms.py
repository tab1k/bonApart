from django import forms
from .models import Reservation, Apartment


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ApartmentForm, self).__init__(*args, **kwargs)
        self.fields['image1'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image2'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image3'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image4'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image5'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image6'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image7'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image8'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image9'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image10'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image11'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image12'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['deal_type'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['city'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['side'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['level'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['rating'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['capacity'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['room'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['square'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['floor'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['total_floors'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['singlebeds'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['doublebeds'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['price'].widget.attrs.update({'class': 'form-control form-control-lg'})


class ApartmentAddForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['image1','deal_type', 'city', 'name', 'address', 'description', 'side',
                  'level', 'rating', 'capacity', 'room', 'square', 'floor',
                  'total_floors', 'elevator', 'singlebeds', 'doublebeds', 'doublebeds',
                  'price', 'wifi', 'air_conditioning', 'parking', 'orthopedic_mattress',
                  'smart_tv', 'hairdryer', 'iron', 'washing_machine', 'bath', 'fridge', 'electric_kettle', 'plate', 'mini_bar', 'hygiene',
                  'dishes', 'shower']

    def __init__(self, *args, **kwargs):
        super(ApartmentAddForm, self).__init__(*args, **kwargs)
        self.fields['image1'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['deal_type'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['city'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['side'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['level'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['rating'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['capacity'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['room'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['square'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['floor'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['total_floors'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['elevator'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['singlebeds'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['doublebeds'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['price'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['wifi'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['air_conditioning'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['parking'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['orthopedic_mattress'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['smart_tv'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['hairdryer'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['iron'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['washing_machine'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['bath'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['fridge'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['electric_kettle'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['plate'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['mini_bar'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['hygiene'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['dishes'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['shower'].widget.attrs.update({'class': 'form-check-input'})


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


    city_choice = forms.ChoiceField(required=False, label='Город')
    class_choice = forms.ChoiceField(choices=CLASS_CHOICES, required=False, label='Класс квартир')
    price_choice = forms.ChoiceField(choices=PRICE_CHOICES, required=False, label='Цена')
    rating_choice = forms.ChoiceField(choices=RATING_CHOICES, required=False, label='Рейтинг')
    additional_choice = forms.MultipleChoiceField(choices=ADDITIONAL_CHOICES, required=False,
                                                  widget=forms.CheckboxSelectMultiple, label='Дополнительно')


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
