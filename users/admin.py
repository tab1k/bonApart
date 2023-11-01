from django.contrib import admin
from users.models import CustomUser, Notification


admin.site.register(CustomUser)
admin.site.register(Notification)