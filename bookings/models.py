from django.db import models
from django.contrib.auth.models import User

class TennisCourt(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    available = models.BooleanField(default=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(TennisCourt, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    duration = models.IntegerField()  # in hours

    def __str__(self):
        return f"{self.user.username} - {self.court.name}"