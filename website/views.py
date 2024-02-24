from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from telegram import Bot
from website.forms import CarFilterForm
from users.forms import CommentForm
from users.models import Notification, FavoriteApartment, Comment
from website.models import *
from django.shortcuts import render
from django.views import View
import requests
from apartments.models import *


class IndexView(View):

    def get(self, request):
        user = request.user
        apartment = Apartment.objects.filter(price__lte=20000)
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')
        cities = City.objects.all()
        context = {
            'user': user,
            'cities': cities,
            'apartment': apartment,
            'notifications' : notifications,
        }
        return render(request, 'website/index.html', context)



class StockView(View):

    def get(self, request):
        stock = Stock.objects.filter(valid=True).order_by('start_date')
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        context = {
            'stock' : stock,
            'notifications': notifications,
        }
        return render(request, 'website/stock.html', context)


class CollaborationView(View):

    def get(self, request):
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        context = {
            'notifications': notifications,
        }

        return render(request, 'website/collaboration.html', context)


class TransfersView(View):

    def get(self, request):
        form = CarFilterForm(request.GET)
        cars = Car.objects.all().order_by('-id')
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        if form.is_valid():
            class_choice = form.cleaned_data['class_choice']
            if class_choice:
                cars = cars.filter(level=class_choice)

        paginator = Paginator(cars, 10)  # 10 - количество элементов на странице

        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {
            'cars': page,
            'form': form,
            'notifications': notifications,
        }
        return render(request, 'website/transfers.html', context)


class AboutView(View):

    def get(self, request):
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        context = {
            'notifications': notifications,
        }

        return render(request, 'website/about-us.html', context)



class PrivacyPolicy(View):

    template_name = 'website/privacy.html'

    def get(self, request):
        return render(request, self.template_name)


class Terms(View):
    template_name = 'website/terms.html'

    def get(self, request):
        return render(request, self.template_name)


class Support(View):
    template_name = 'website/help_center.html'

    def get(self, request):
        return render(request, self.template_name)











