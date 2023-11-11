from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('apartments', ApartmentView.as_view(), name='apartments'),
    path('apartments/<int:apartment_id>/reserve/', ApartmentView.as_view(), name='apartment_reserve'),
    path('success_reservation', SuccessReservation.as_view(), name='success_reservation'),
    path('apartments/add_to_favorite/<int:apartment_id>/', ApartmentView.as_view(), name='add_to_favorite'),
    path('stock', StockView.as_view(), name='stock'),
    path('collaboration', CollaborationView.as_view(), name='collaboration'),
    path('transfers', TransfersView.as_view(), name='transfers'),
    path('about', AboutView.as_view(), name='about'),
    path('apartaments-detail/<int:pk>/', ApartamentsDetailView.as_view(), name='apartaments-detail'),
    path('privacy_policy', PrivacyPolicy.as_view(), name='privacy_policy'),
    path('terms', Terms.as_view(), name='terms'),
    path('support', Support.as_view(), name='support')

]
