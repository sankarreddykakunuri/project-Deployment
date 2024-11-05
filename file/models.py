from django.db import models
from django.contrib.auth.models import User  # Assuming you might need User for seller

class Bike(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming a seller relationship
    # Add other fields as needed

    def __str__(self):
        return self.name
