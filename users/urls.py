from django.urls import path
from users.views import *
from django.contrib.auth.views import LogoutView


app_name = 'users'

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('notifications/', NotificationView.as_view(), name='notifications'),
    path('mark_notification_as_read/<int:notification_id>/', mark_notification_as_read, name='mark_notification_as_read'),
    path('my-apartments/', UserApartmentsListView.as_view(), name='my-apartments'),
    path('delete_profile/', DeleteProfileView.as_view(), name='delete_profile'),

    path('favorites/', FavoritesView.as_view(), name='favorites'),
    path('clear_favorites/', ClearFavoritesView.as_view(), name='clear_favorites'),
    path('pending/', ApartmentPendingListView.as_view(), name='apartment_pending'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
