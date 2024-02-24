from django.contrib import admin
from apartments.models import *


admin.site.register(Apartment)
admin.site.register(Reservation)
admin.site.register(GeoPosition)
admin.site.register(Discount)
