from django.db import models
from django.conf import settings

class BookingUser(models.Model):
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    nationality = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.email}'

class Booking(models.Model):
    user = models.ForeignKey(BookingUser, on_delete=models.CASCADE)
    boatschedule = = models.ForeignKey(BoatSchedule, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=False=True)
    total_ticket = models.SmallInterger()
    is_paid = models.Boolean(default=False)
    
    def __str__(self):
        return f'{self.user.email} - {self.boatschedule.from} - {self.boatschedule.to}'


user_id
boatschedule_id
datetime
total_ticket
is_paid

BoatSchedule
id
from
to
ferry_type
Datetime
price




class booking(models.Model):


{
    "id": "PD2124",
    "is_approve": false,
    "booking_no": "PD2124",
    "name": "David Soraham",
    "email": "david.ham@gmail.com",
    "total_ticket": "2",
    "from": "Koh Phi Phi",
    "to": "Krabi",
    "time": "11:00 - 12:00",
    "ferry": "Speedboat"
},