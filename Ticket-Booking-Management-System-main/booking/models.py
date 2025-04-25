from django.db import models
from accounts.models import CustomUser

class Show(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    duration = models.DurationField()
    venue = models.CharField(max_length=200)
    total_seats = models.PositiveIntegerField()
    price_per_seat = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} at {self.venue} on {self.date.strftime('%Y-%m-%d %H:%M')}"

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.email} booked {self.seats} seats for {self.show.title}"