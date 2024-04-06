from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileUpdateForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View
from users.models import FavoriteApartment, Apartment  
from django.shortcuts import redirect
from .models import Notification
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


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
        form = UserProfileUpdateForm(instance=user)  

        context = {
            'user': user,
            'form': form,  
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


class FavoritesView(LoginRequiredMixin, ListView):
    model = FavoriteApartment
    template_name = 'user_templates/favorites.html'
    context_object_name = 'favorite_apartments'

    def get_queryset(self):
        return FavoriteApartment.objects.filter(user=self.request.user)



class ClearFavoritesView(LoginRequiredMixin, View):
    def post(self, request):
        
        favorites = FavoriteApartment.objects.filter(user=request.user)
        apartment_id = request.POST.get('remove_favorite')

        if apartment_id:
            FavoriteApartment.objects.filter(user=request.user, apartment_id=apartment_id).delete()
            messages.success(request, 'Квартира успешно удалена из избранного.')

            return HttpResponseRedirect(reverse('users:favorites'))

        
        favorites.delete()

        
        messages.success(request, 'Избранные квартиры успешно очищены.')

        
        return HttpResponseRedirect(reverse('users:favorites'))


class DeleteProfileView(LoginRequiredMixin, View):
    template_name = 'user_templates/delete_profile.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        
        request.user.delete()
        
        logout(request)
        
        return redirect('website:home')


class ApartmentPendingListView(LoginRequiredMixin, ListView):
    template_name = 'user_templates/apartments_pending_list.html'
    model = Apartment
    context_object_name = 'apartments'
    paginate_by = 10

    def get_queryset(self):
        return Apartment.objects.filter(status='pending')



class UserApartmentsListView(LoginRequiredMixin, ListView):
    model = Apartment
    template_name = 'user_templates/my_apartments.html'
    context_object_name = 'user_apartments'

    def get_queryset(self):
        return Apartment.objects.filter(owner=self.request.user)

