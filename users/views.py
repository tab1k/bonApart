from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileUpdateForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Notification
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from .models import FavoriteApartment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View
from django.shortcuts import render, redirect
from users.models import FavoriteApartment, Apartment  # Замените 'your_app' на имя вашего приложения
from django.shortcuts import redirect
from .models import Notification
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render


class SignInView(LoginView):
    template_name = 'signin.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('website:home')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('users:signin')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)



def error_404_view(request, exception):
    return render(request, 'website/404.html', status=404)


class ProfileView(View):
    template_name = 'user_templates/user_profile.html'

    def get(self, request):
        user = request.user
        form = UserProfileUpdateForm(instance=user)  # Создайте форму с текущими данными пользователя

        context = {
            'user': user,
            'form': form,  # Передайте форму в контекст
        }

        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        form = UserProfileUpdateForm(request.POST, instance=user)
        password_form = PasswordChangeForm(user, request.POST)

        if form.is_valid():
            form.save()
            return redirect('website:home')

        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Пароль успешно изменен.')
        else:
            messages.success(request, 'Пароль не изменен!')

        context = {
            'user': user,
            'form': form,
            'password_form': password_form,
        }

        return render(request, self.template_name, context)


class NotificationView(View):
    template_name = 'user_templates/notifications.html'

    def get(self, request):
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')
        return render(request, self.template_name, {'notifications': notifications})

    def create_notifications_for_users(self, event_type, message, photo=None, link=None):
        users = User.objects.all()
        for user in users:
            Notification.objects.create(
                event_type=event_type,
                message=message,
                user=user,
                photo=photo,
                link=link
            )

    def post(self, request):
        notification_id = request.POST.get('notification_id')
        if notification_id:
            notification = Notification.objects.get(pk=notification_id)
            notification.read = True
            notification.save()
        return redirect('users:notifications')



def mark_notification_as_read(request, notification_id):
    notification = Notification.objects.get(pk=notification_id)
    notification.read = True
    notification.save()
    return redirect('your_notification_page_name')




class FavoritesView(View):
    template_name = 'user_templates/favorites.html'

    def get(self, request):
        user = request.user
        favorite_apartments = FavoriteApartment.objects.filter(user=user).select_related('apartment')

        context = {
            'favorite_apartments': favorite_apartments,
        }

        return render(request, self.template_name, context)


class DeleteProfileView(LoginRequiredMixin, View):
    template_name = 'user_templates/delete_profile.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # Удалите профиль пользователя
        request.user.delete()
        # Разлогиньте пользователя после удаления
        logout(request)
        # Перенаправьте пользователя на страницу, где будет подтверждение удаления или другую страницу
        return redirect('website:home')



