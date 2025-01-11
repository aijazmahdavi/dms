from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Donor(models.Model):
    PREFIX_CHOICES = [
        ('syed', 'Syed'),
        ('mirza', 'Mirza'),
        ('shaikh', 'shaikh'),
        ('other', 'other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES, default='other')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Mustahiq(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    need_category = models.CharField(max_length=100)  # e.g., Education, Medical, Housing
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    total_received = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.get_full_name() or self.user.username