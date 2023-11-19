from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from telegram import Bot
from users.forms import CommentForm
from users.models import Notification, FavoriteApartment, Comment
from .forms import ApartmentFilterForm, CarFilterForm, ReservationForm
from website.models import *
from django.shortcuts import render
from django.views import View
import requests


class IndexView(View):

    def get(self, request):
        user = request.user
        apartment = Apartment.objects.filter(price__lte=20000)
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')
        context = {
            'user': user,
            'apartment': apartment,
            'notifications' : notifications,
        }
        return render(request, 'website/index.html', context)


class SearchResultsView(View):
    class SearchResultsView(View):
        template_name = 'website/search_results.html'

        def post(self, request):
            # Обработка POST-запроса и выполнение поиска
            class_choice = request.POST.get('class_choice')
            price_choice = request.POST.get('price_choice')
            rating_choice = request.POST.get('rating_choice')
            # Дополнительная логика поиска на основе формы

            # Перенаправление на страницу с результатами поиска
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
            # Получите квартиру, которую пользователь хочет забронировать
            apartment = Apartment.objects.get(id=apartment_id)
            form.save()

            return self.send_telegram_message(apartment, form)

        else:
            if request.POST.get('action') == 'add_to_favorites':
                # Добавление квартиры в избранное
                apartment_id = request.POST.get('apartment_id')

                # Проверьте, что пользователь аутентифицирован
                if request.user.is_authenticated:
                    # Попробуйте найти запись в базе данных, чтобы избежать дублирования
                    existing_favorite = FavoriteApartment.objects.filter(user=request.user,
                                                                         apartment_id=apartment_id).first()

                    if not existing_favorite:
                        # Создайте новую запись в избранном
                        favorite = FavoriteApartment(user=request.user, apartment_id=apartment_id)
                        favorite.save()

                        # После успешного добавления в избранное, вы можете выполнить дополнительные действия
                        return redirect('users:favorites')  # Перенаправьте пользователя на страницу избранных квартир
                    else:
                        # Если запись уже существует, вы можете выполнить другие действия или вернуть сообщение пользователю
                        return redirect('users:favorites')
                else:
                    # Если пользователь не аутентифицирован, перенаправьте его на страницу входа или выполните другие действия
                    return redirect('users:signin')
            else:
                apartments = Apartment.objects.all()
                context = {'apartments': apartments, 'form': form}
                return render(request, self.template_name, context)


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


class ApartamentsDetailView(View):

    TELEGRAM_BOT_TOKEN = '6709416090:AAFayt-eVfuaYUYKUHjkt4FGKEHUgO7Oo6E'
    TELEGRAM_CHAT_ID = '-1002073862577'

    def get(self, request, pk):
        try:
            apartments_detail = Apartment.objects.get(pk=pk)
            geo_queryset = GeoPosition.objects.filter(apartment=apartments_detail)
            geo = geo_queryset.first()  # Choose the first object
        except Apartment.DoesNotExist:
            raise Http404("Apartment does not exist")
        except GeoPosition.MultipleObjectsReturned:
            # Handle the case where multiple GeoPosition objects are returned
            # You might want to redirect to a specific page or log a message
            raise Http404("Multiple GeoPosition objects found for the Apartment")
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')
        comments = Comment.objects.filter(apartment=apartments_detail)
        comment_form = CommentForm()  # Создайте экземпляр формы для комментариев


        context = {
            'geo' : geo,
            'detail': apartments_detail,
            'comments': comments,
            'notifications': notifications,
            'comment_form': comment_form,  # Передайте форму в контекст
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
        comment_form = CommentForm(request.POST)  # Получите данные POST-запроса

        form = ReservationForm(request.POST)

        if form.is_valid():
            # Получите квартиру, которую пользователь хочет забронировать
            apartment = Apartment.objects.get(id=pk)
            form.save()

            return self.send_telegram_message(apartment, form)

        if comment_form.is_valid():
            if request.user.is_authenticated:
                new_comment = comment_form.save(commit=False)
                new_comment.apartment = apartments_detail
                new_comment.user = request.user  # Привяжите комментарий к текущему пользователю
                new_comment.save()
                return redirect('website:apartments')  # Перенаправьте пользователя на страницу квартиры
            else:
                return redirect('users:signup')

        # Если форма не действительна, возвращайтесь на ту же страницу
        comments = Comment.objects.filter(apartment=apartments_detail)
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        context = {
            'detail': apartments_detail,
            'comments': comments,
            'notifications': notifications,
            'comment_form': comment_form,
        }

        return render(request, 'website/apartments_list.html', context)



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


class SuccessReservation(View):

    def get(self, request):
        return render(request, 'website/success.html')





