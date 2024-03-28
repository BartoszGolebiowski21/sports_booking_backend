from django.db import models


class SportsFacility(models.Model):
    name = models.CharField(max_length=63, null=True, blank=True)
    facility_type = models.CharField(max_length=63, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Sports Facilities"


class Reservation(models.Model):
    facility = models.ForeignKey(SportsFacility, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    light_on = models.BooleanField(null=True, blank=True)
    made_by = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.facility} - {self.date} - {self.made_by}'