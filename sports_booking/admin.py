from django.contrib import admin

from sports_booking import models

admin.site.register(models.SportsFacility)
class SportsFacilityAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(models.Reservation)
