from django.urls import path
from apartments.views import *
from django.contrib.auth.views import LogoutView

app_name = 'apartments'

urlpatterns = [

    # path('buy/apartments/', ApartmentBuyView.as_view(), name='buy'),
    # path('rent/', RentView.as_view(), name='rent'),

    # RECONSTRUCT

    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('', ApartmentView.as_view(), name='apartments'),
    path('apartaments-detail/<int:pk>/', ApartamentsDetailView.as_view(), name='apartaments-detail'),
    path('<int:apartment_id>/reserve/', ApartmentView.as_view(), name='apartment_reserve'),
    path('success_reservation', SuccessReservation.as_view(), name='success_reservation'),
    path('add_to_favorite/<int:apartment_id>/', ApartmentView.as_view(), name='add_to_favorite'),
]
