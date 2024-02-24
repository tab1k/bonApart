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
                  'smart_tv', 'hairdryer', 'iron', 'washing_machine', 'bath']

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


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'surname', 'phone']
