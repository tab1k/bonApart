from django.shortcuts import render, redirect
from django.views import View
from apartments.forms import *
from .forms import ApartmentFilterForm, ReservationForm
from apartments.models import *
from users.models import *
from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from users.forms import CommentForm

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
        apartments = Apartment.objects.all().order_by('-id')
        discount = Discount.objects.filter(apartment__in=apartments)
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        if form.is_valid():
            class_choice = form.cleaned_data['class_choice']
            price_choice = form.cleaned_data['price_choice']
            rating_choice = form.cleaned_data['rating_choice']
            additional_choice = form.cleaned_data['additional_choice']

            if class_choice:
                apartments = apartments.filter(level=class_choice)

            if price_choice:
                if price_choice == '1':
                    apartments = apartments.filter(price__gte=10000)
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
        }
        return render(request, self.template_name, context)

    def send_telegram_message(self, apartment, form):
        try:
            bot_token = self.TELEGRAM_BOT_TOKEN
            chat_id = self.TELEGRAM_CHAT_ID
            message = f'Пользователь забронировал квартиру:\n\n'
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
                return redirect('website:success_reservation')
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

        context = {
            'geo': geo,
            'detail': apartments_detail,
            'comments': comments,
            'notifications': notifications,
            'comment_form': comment_form,
        }

        return render(request, 'website/detail.html', context)

    def send_telegram_message(self, apartment, form):
        try:
            bot_token = self.TELEGRAM_BOT_TOKEN
            chat_id = self.TELEGRAM_CHAT_ID
            message = f'Пользователь забронировал квартиру:\n\n'
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
                return redirect('website:success_reservation')
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


class SuccessReservation(View):

    def get(self, request):
        return render(request, 'website/success.html')





