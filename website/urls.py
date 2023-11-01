from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('apartments', ApartmentView.as_view(), name='apartments'),
    path('stock', StockView.as_view(), name='stock'),
    path('collaboration', CollaborationView.as_view(), name='collaboration'),
    path('transfers', TransfersView.as_view(), name='transfers'),
    path('about', AboutView.as_view(), name='about'),
    path('apartaments-detail/<int:pk>/', ApartamentsDetailView.as_view(), name='apartaments-detail'),
]
