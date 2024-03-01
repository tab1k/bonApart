from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites import requests
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from apartments.forms import *
from .forms import ApartmentFilterForm, ReservationForm
from apartments.models import *
from users.models import *
from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from users.forms import CommentForm
import requests



class SearchResultsView(View):
    template_name = 'website/search_results.html'

    def post(self, request):
        class_choice = request.POST.get('class_choice')
        price_choice = request.POST.get('price_choice')
        rating_choice = request.POST.get('rating_choice')

        return redirect('search_results', class_choice=class_choice, price_choice=price_choice,
                        rating_choice=rating_choice)


class ApartmentView(View):
    template_name = 'website/apartments_list.html'
    TELEGRAM_BOT_TOKEN = '6709416090:AAFayt-eVfuaYUYKUHjkt4FGKEHUgO7Oo6E'
    TELEGRAM_CHAT_ID = '-1002073862577'

    def get(self, request):

        form = ApartmentFilterForm(request.GET)
        cities = City.objects.all()
        apartments = Apartment.objects.filter(status='approved').order_by('-timestamp')
        discount = Discount.objects.filter(apartment__in=apartments)
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')
        selected_city = request.GET.get('selected_city')

        if selected_city:
            apartments = Apartment.objects.filter(city__name=selected_city, status='approved')
        else:
            apartments = Apartment.objects.filter(status='approved')

        for apartment in apartments:
            if apartment.owner:
                owner_phone = apartment.owner.phone_number
            else:
                owner_phone = None

        if form.is_valid():
            class_choice = form.cleaned_data['class_choice']
            price_choice = form.cleaned_data['price_choice']
            rating_choice = form.cleaned_data['rating_choice']
            additional_choice = form.cleaned_data['additional_choice']
            city_choice = form.cleaned_data['city_choice']

            if city_choice:
                apartments = apartments.filter(city__name=city_choice, status='approved')
            else:
                apartments = apartments.filter(status='approved')

            if class_choice:
                apartments = apartments.filter(level=class_choice)

            if price_choice:
                if price_choice == '1':
                    apartments = apartments.filter(price__gte=10000, city__name=selected_city)
                elif price_choice == '2':
                    apartments = apartments.filter(price__range=(10000, 15000))
                elif price_choice == '3':
                    apartments = apartments.filter(price__range=(15000, 20000))
                elif price_choice == '4':
                    apartments = apartments.filter(price__range=(20000, 25000))
                elif price_choice == '5':
                    apartments = apartments.filter(price__gte=25000)

            if rating_choice:
                apartments = apartments.filter(rating=rating_choice)

            if rating_choice:
                apartments = apartments.filter(rating=rating_choice)

            if additional_choice:
                for option in additional_choice:
                    apartments = apartments.filter(**{option: True})

        paginator = Paginator(apartments, 10)  # 10 - количество элементов на странице

        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {
            'apartment': page,
            'form': form,
            'discount': discount,
            'notifications': notifications,
            'cities': cities,
            'selected_city': selected_city,
            'owner_phone': owner_phone,
        }
        return render(request, self.template_name, context)

    def send_telegram_message(self, apartment, form):
        try:
            bot_token = self.TELEGRAM_BOT_TOKEN
            chat_id = self.TELEGRAM_CHAT_ID
            message = ''

            if apartment.deal_type == 'daily_rent':
                message = f'Пользователь забронировал квартиру на аренду по суточно:\n\n'
            elif apartment.deal_type == 'monthly_rent':
                message = f'Пользователь забронировал квартиру на аренду помесячно:\n\n'
            elif apartment.deal_type == 'sale':
                message = f'Пользователь хочет купить квартиру:\n\n'
            else:
                return JsonResponse({'error': 'Неизвестный тип сделки!'})

            message += f'Жилой комплекс: {apartment.name}\n'
            message += f'Имя: {form.cleaned_data["name"]}\n'
            message += f'Фамилия: {form.cleaned_data["surname"]}\n'
            message += f'Телефон: {form.cleaned_data["phone"]}\n'

            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            data = {
                'chat_id': chat_id,
                'text': message
            }
            response = requests.post(url, data=data)

            if response.status_code == 200:
                return redirect('apartments:success_reservation')
            else:
                return JsonResponse({'error': 'Не удалось отправить сообщение!'})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    def post(self, request, apartment_id):

        form = ReservationForm(request.POST)

        if form.is_valid():

            apartment = Apartment.objects.get(id=apartment_id)
            form.save()

            return self.send_telegram_message(apartment, form)

        else:
            if request.POST.get('action') == 'add_to_favorites':

                apartment_id = request.POST.get('apartment_id')

                if request.user.is_authenticated:

                    existing_favorite = FavoriteApartment.objects.filter(user=request.user,
                                                                         apartment_id=apartment_id).first()

                    if not existing_favorite:

                        favorite = FavoriteApartment(user=request.user, apartment_id=apartment_id)
                        favorite.save()

                        return redirect('users:favorites')
                    else:

                        return redirect('users:favorites')
                else:

                    return redirect('users:signin')
            else:
                apartments = Apartment.objects.all()
                context = {'apartments': apartments, 'form': form}
                return render(request, self.template_name, context)


class ApartamentsDetailView(View):
    TELEGRAM_BOT_TOKEN = '6709416090:AAFayt-eVfuaYUYKUHjkt4FGKEHUgO7Oo6E'
    TELEGRAM_CHAT_ID = '-1002073862577'

    def get(self, request, pk):
        try:
            apartments_detail = Apartment.objects.get(pk=pk)
            geo_queryset = GeoPosition.objects.filter(apartment=apartments_detail)
            geo = geo_queryset.first()
        except Apartment.DoesNotExist:
            raise Http404("Apartment does not exist")
        except GeoPosition.MultipleObjectsReturned:

            raise Http404("Multiple GeoPosition objects found for the Apartment")
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')
        comments = Comment.objects.filter(apartment=apartments_detail)
        comment_form = CommentForm()

        if apartments_detail.owner:
            owner_phone = apartments_detail.owner.phone_number
        else:
            owner_phone = None
        context = {
            'geo': geo,
            'detail': apartments_detail,
            'comments': comments,
            'notifications': notifications,
            'comment_form': comment_form,
            'owner_phone': owner_phone,
        }

        return render(request, 'website/detail.html', context)

    def send_telegram_message(self, apartment, form):
        try:
            bot_token = self.TELEGRAM_BOT_TOKEN
            chat_id = self.TELEGRAM_CHAT_ID
            message = ''

            if apartment.deal_type == 'daily_rent':
                message = f'Пользователь забронировал квартиру на аренду по суточно:\n\n'
            elif apartment.deal_type == 'monthly_rent':
                message = f'Пользователь забронировал квартиру на аренду помесячно:\n\n'
            elif apartment.deal_type == 'sale':
                message = f'Пользователь хочет купить квартиру:\n\n'
            else:
                return JsonResponse({'error': 'Неизвестный тип сделки!'})

            message += f'Жилой комплекс: {apartment.name}\n'
            message += f'Имя: {form.cleaned_data["name"]}\n'
            message += f'Фамилия: {form.cleaned_data["surname"]}\n'
            message += f'Телефон: {form.cleaned_data["phone"]}\n'

            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            data = {
                'chat_id': chat_id,
                'text': message
            }
            response = requests.post(url, data=data)

            if response.status_code == 200:
                return redirect('apartments:success_reservation')
            else:
                return JsonResponse({'error': 'Не удалось отправить сообщение!'})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    def post(self, request, pk):
        apartments_detail = Apartment.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)

        form = ReservationForm(request.POST)

        if form.is_valid():
            apartment = Apartment.objects.get(id=pk)
            form.save()

            return self.send_telegram_message(apartment, form)

        if comment_form.is_valid():
            if request.user.is_authenticated:
                new_comment = comment_form.save(commit=False)
                new_comment.apartment = apartments_detail
                new_comment.user = request.user
                new_comment.save()
                return redirect('apartments:apartments')
            else:
                return redirect('users:signup')

        comments = Comment.objects.filter(apartment=apartments_detail)
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        context = {
            'detail': apartments_detail,
            'comments': comments,
            'notifications': notifications,
            'comment_form': comment_form,
        }

        return render(request, 'website/apartments_list.html', context)


class ApartamentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Apartment
    form_class = ApartmentForm
    template_name = 'apartments/apartments_update.html'

    def get_success_url(self):
        return reverse_lazy('apartments:apartaments_edit', kwargs={'pk': self.object.pk})


class SuccessReservation(View):

    def get(self, request):
        return render(request, 'website/success.html')


class ApartmentBuyView(ListView):
    template_name = 'apartments/apartments_buy.html'
    context_object_name = 'apartment'
    form_class = ApartmentBuyFilterForm

    def get_queryset(self):
        selected_city = self.request.GET.get('selected_city')
        queryset = Apartment.objects.filter(deal_type='sale', status='approved')
        if selected_city:
            queryset = queryset.filter(city__name=selected_city, status='approved')

        form = self.form_class(self.request.GET)


        if form.is_valid():
            floor_choice = form.cleaned_data.get('floor_choice')
            room_choice = form.cleaned_data.get('room_choice')
            square_choice = form.cleaned_data.get('square_choice')
            price_from = form.cleaned_data.get('price_from')
            price_to = form.cleaned_data.get('price_to')

            # Применение фильтров к queryset
            if floor_choice:
                queryset = queryset.filter(floor=floor_choice)
            if room_choice:
                queryset = queryset.filter(room=room_choice)
            if square_choice:
                queryset = queryset.filter(square=square_choice)
            if price_from:
                queryset = queryset.filter(price__gte=price_from)
            if price_to:
                queryset = queryset.filter(price__lte=price_to)

        return queryset.order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['form'] = self.form_class(self.request.GET)

        # Определение owner_phone
        owner_phone = None
        selected_city = self.request.GET.get('selected_city')
        queryset = Apartment.objects.filter(deal_type='sale', status='approved')
        if selected_city:
            queryset = queryset.filter(city__name=selected_city, status='approved')

        # Проверяем, есть ли владелец у первой квартиры в queryset
        first_apartment = queryset.first()
        if first_apartment and first_apartment.owner:
            owner_phone = first_apartment.owner.phone_number

        context['owner_phone'] = owner_phone

        return context


class ApartmentRentView(ListView):
    template_name = 'apartments/apartments_rent.html'
    context_object_name = 'apartment'

    def get_queryset(self):
        selected_city = self.request.GET.get('selected_city')
        queryset = Apartment.objects.filter(status='approved')

        if selected_city:
            queryset = queryset.filter(city__name=selected_city)

        queryset = queryset.filter(Q(deal_type='monthly_rent') | Q(deal_type='daily_rent'))

        return queryset.order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()

        # Определение owner_phone
        owner_phone = None
        selected_city = self.request.GET.get('selected_city')
        queryset = Apartment.objects.filter(status='approved')

        if selected_city:
            queryset = queryset.filter(city__name=selected_city)

        queryset = queryset.filter(Q(deal_type='monthly_rent') | Q(deal_type='daily_rent'))

        # Проверяем, есть ли владелец у первой квартиры в queryset
        first_apartment = queryset.first()
        if first_apartment and first_apartment.owner:
            owner_phone = first_apartment.owner.phone_number

        context['owner_phone'] = owner_phone

        return context


class ApartmentRentBaseView(ListView):
    template_name = ''
    context_object_name = 'apartment'
    deal_type = None

    def get_template_names(self):
        if self.template_name:
            return [self.template_name]
        raise ImproperlyConfigured("Template name not specified")

    def get_queryset(self):
        selected_city = self.request.GET.get('selected_city')
        queryset = Apartment.objects.filter(deal_type=self.deal_type, status='approved')

        if selected_city:
            queryset = queryset.filter(city__name=selected_city)

        return queryset.order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()  # Add cities to the context
        if self.deal_type == 'daily_rent':
            context['form'] = ApartmentFilterForm(self.request.GET)
        elif self.deal_type == 'monthly_rent':
            context['form'] = ApartmentBuyFilterForm(self.request.GET)

        # Определение owner_phone
        owner_phone = None
        selected_city = self.request.GET.get('selected_city')
        queryset = Apartment.objects.filter(deal_type=self.deal_type, status='approved')

        if selected_city:
            queryset = queryset.filter(city__name=selected_city)

        # Проверяем, есть ли владелец у первой квартиры в queryset
        first_apartment = queryset.first()
        if first_apartment and first_apartment.owner:
            owner_phone = first_apartment.owner.phone_number

        context['owner_phone'] = owner_phone

        return context


class ApartmentRentDayView(ApartmentRentBaseView):
    template_name = 'apartments/apartments_rent_day.html'
    deal_type = 'daily_rent'


class ApartmentRentMonthView(ApartmentRentBaseView):
    template_name = 'apartments/apartments_rent_month.html'
    deal_type = 'monthly_rent'


class ApartmentAddView(LoginRequiredMixin, CreateView):
    template_name = 'apartments/apartments_add.html'
    model = Apartment
    form_class = ApartmentAddForm
    success_url = reverse_lazy('apartments:apartments')

    def form_valid(self, form):
        # Устанавливаем статус квартиры как "На рассмотрении"
        form.instance.status = 'pending'

        # Устанавливаем владельца квартиры в текущего пользователя
        form.instance.owner = self.request.user

        # Сохраняем квартиру
        self.object = form.save()

        # Получаем текущего пользователя
        user = self.request.user

        # Присваиваем объект квартиры полю apartments текущего пользователя
        user.apartments = self.object
        user.save()

        # Добавляем сообщение об успешном добавлении квартиры для пользователя
        messages.success(self.request, 'Квартира была добавлена и находится на рассмотрении администратора.')

        return super().form_valid(form)


class ApartmentApproveView(View):
    def post(self, request, pk):
        apartment = get_object_or_404(Apartment, pk=pk)
        apartment.status = 'approved'
        apartment.save()
        if apartment.owner and apartment.status == 'approved':

            message = f"Ваша квартира '{apartment.name}' была одобрена!"

            messages.success(request, message)

        return redirect('apartments:apartaments-detail', pk=pk)


class ApartmentRejectView(View):
    def post(self, request, pk):
        apartment = get_object_or_404(Apartment, pk=pk)
        apartment.delete()
        messages.success(request, 'Квартира удалена!')
        return redirect('users:apartment_pending')



