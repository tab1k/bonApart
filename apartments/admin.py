from django.contrib import admin
from apartments.models import *


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'approval_date', 'expiry_date', 'archived_display']
    list_filter = ['status']
    actions = ['restore_selected']

    def restore_selected(self, request, queryset):
        # Восстанавливаем выбранные квартиры из архива
        queryset.update(archived=False)
        self.message_user(request, "Выбранные квартиры были успешно восстановлены из архива.")

    restore_selected.short_description = "Восстановить выбранные квартиры из архива"

    def archived_display(self, obj):
        return obj.archived
    archived_display.boolean = True
    archived_display.short_description = 'Archived'


admin.site.register(Apartment, ApartmentAdmin)

admin.site.register(Reservation)
admin.site.register(GeoPosition)
admin.site.register(Discount)
admin.site.register(City)
