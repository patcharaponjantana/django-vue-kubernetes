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


class FerryType(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.name}'

class BoatSchedule(models.Model):
    from_location = models.CharField(max_length=300)
    to_location = models.CharField(max_length=300)
    ferry_type = models.ForeignKey(FerryType, on_delete=models.CASCADE)
    departure_datetime = models.DateTimeField()
    price = models.FloatField()
    
    def __str__(self):
        return f'{self.from_location} - {self.to_location} - {self.departure_datetime}'

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
