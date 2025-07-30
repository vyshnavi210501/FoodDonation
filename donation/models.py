from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_item} by {self.donor.username}"
