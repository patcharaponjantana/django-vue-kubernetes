from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.FerryType)
admin.site.register(models.BoatSchedule)
admin.site.register(models.Booking)
# admin.site.register(models.BookingUser)