from django.urls import path
from apartments.views import *
from django.contrib.auth.views import LogoutView

app_name = 'apartments'

urlpatterns = [

    path('buy/', ApartmentBuyView.as_view(), name='buy'),
    path('rent/', ApartmentRentView.as_view(), name='rent'),
    path('rent/day/', ApartmentRentDayView.as_view(), name='apartment-rent-day'),
    path('rent/month/', ApartmentRentMonthView.as_view(), name='apartment-rent-month'),
    path('add/', ApartmentAddView.as_view(), name='add'),
    path('archived-apartments/', ArchivedApartmentView.as_view(), name='archived_apartments'),

    path('<int:pk>/approve/', ApartmentApproveView.as_view(), name='approve'),
    path('<int:pk>/reject/', ApartmentRejectView.as_view(), name='reject'),
    # RECONSTRUCT

    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('', ApartmentView.as_view(), name='apartments'),
    path('apartaments-detail/<int:pk>/', ApartamentsDetailView.as_view(), name='apartaments-detail'),

    path('apartaments-detail/<int:pk>/toggle-booking/', ToggleBookingView.as_view(), name='toggle_booking'),
    path('apartaments-detail/<int:pk>/occupied-dates/', OccupiedDatesView.as_view(), name='occupied_dates'),

    path('apartaments-detail/<int:pk>/edit', ApartamentsUpdateView.as_view(), name='apartaments_edit'),
    path('<int:apartment_id>/reserve/', ApartmentView.as_view(), name='apartment_reserve'),
    path('success_reservation', SuccessReservation.as_view(), name='success_reservation'),
    path('add_to_favorite/<int:apartment_id>/', ApartmentView.as_view(), name='add_to_favorite'),
]
