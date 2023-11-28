from django.db import models
from django.conf import settings

# class BookingUser(models.Model):
#     user =  models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     first_name = models.CharField(max_length=300)
#     last_name = models.CharField(max_length=300)
#     email = models.EmailField()
#     nationality = models.CharField(max_length=50)
    
#     def __str__(self):
#         return f'{self.first_name} - {self.last_name} - {self.email}'
class Location(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.name}'

class FerryType(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.name}'

class BoatSchedule(models.Model):
    from_location = models.ForeignKey(Location, related_name='from_location', on_delete=models.CASCADE)
    to_location = models.ForeignKey(Location, related_name='to_location', on_delete=models.CASCADE)
    ferry_type = models.ForeignKey(FerryType, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrive_time = models.DateTimeField()
    price = models.FloatField()
    
    def __str__(self):
        return f'{self.from_location} - {self.to_location} - departure: {self.departure_time} - arrive: {self.arrive_time}'

class Booking(models.Model):
    # user = models.ForeignKey(BookingUser, on_delete=models.CASCADE)
    # user data
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    nationality = models.CharField(max_length=50)


    boatschedule = models.ForeignKey(BoatSchedule, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    total_ticket = models.SmallIntegerField()
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.email} - {self.boatschedule.from_location} - {self.boatschedule.to_location}'
