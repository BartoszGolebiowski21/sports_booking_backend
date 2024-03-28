from django.contrib import admin

from sports_booking import models

admin.site.register(models.SportsFacility)
admin.site.register(models.Reservation)
