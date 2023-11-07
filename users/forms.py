from django import forms
from users.models import CustomUser, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control fakepassword'}),
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'phone_number')

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control fakepassword'}),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    phone_number = forms.CharField(
        label='Номер телефона',
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
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )

    # Пример стилизации для поля last_name
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )

    # Пример стилизации для поля email
    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )

    # Пример стилизации для поля phone_number
    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )

    city = forms.CharField(
        max_length=100,
        label='Город',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,  # Для разрешения пустых значений
    )

    address = forms.CharField(
        label='Адрес',
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'style': 'border: 1px solid #ddd; border-radius: 5px;'})
    )


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Подтвердите новый пароль', widget=forms.PasswordInput)


class CommentForm(forms.ModelForm):
    text = forms.CharField(label='Комментарий:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Comment
        fields = ['text']


class AddToFavoriteForm(forms.Form):
    apartment_id = forms.IntegerField(widget=forms.HiddenInput())


