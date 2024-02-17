from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('stock', StockView.as_view(), name='stock'),
    path('collaboration', CollaborationView.as_view(), name='collaboration'),
    path('transfers', TransfersView.as_view(), name='transfers'),
    path('about', AboutView.as_view(), name='about'),
    path('privacy_policy', PrivacyPolicy.as_view(), name='privacy_policy'),
    path('terms', Terms.as_view(), name='terms'),
    path('support', Support.as_view(), name='support')

]
