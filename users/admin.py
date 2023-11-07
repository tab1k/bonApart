from django.contrib import admin
from users.models import *


admin.site.register(CustomUser)
admin.site.register(Notification)
admin.site.register(Comment)
admin.site.register(FavoriteApartment)