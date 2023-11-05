from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control fakepassword'}),
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'phone_number')

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control fakepassword'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )


class UserProfileUpdateForm(forms.ModelForm):


    GENDER_CHOICES = (
        ('male', 'Мужской'),
        ('female', 'Женский'),
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'city', 'address']

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )

    # Пример стилизации для поля last_name
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )

    # Пример стилизации для поля email
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )

    # Пример стилизации для поля phone_number
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )

    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,  # Для разрешения пустых значений
    )

    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Подтвердите новый пароль', widget=forms.PasswordInput)


