from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Notification

class SignInView(LoginView):
    template_name = 'signin.html'

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
    return render(request, '404.html', status=404)


class ProfileView(View):
    template_name = 'user_templates/user_profile.html'

    def get(self, request):

        user = request.user

        context = {
            'user' : user,
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


from django.shortcuts import redirect
from .models import Notification


def mark_notification_as_read(request, notification_id):
    notification = Notification.objects.get(pk=notification_id)
    notification.read = True
    notification.save()
    return redirect('your_notification_page_name')
