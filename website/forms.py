from django import forms


class CarFilterForm(forms.Form):

    CLASS_CHOICES = (
        ('comfort', 'Комфорт'),
        ('business', 'Бизнес'),
    )

    class_choice = forms.ChoiceField(choices=CLASS_CHOICES,
                                     required=False,
                                     label='Класс машины')

