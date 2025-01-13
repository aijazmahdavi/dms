from django.db import models
from django.contrib.auth.models import User

PREFIX_CHOICES = [
        ('syed', 'Syed'),
        ('mirza', 'Mirza'),
        ('shaikh', 'shaikh'),
        ('other', 'other'),
    ]

# Create your models here.
class Donor(models.Model):
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES, default='other')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Mustahiq(models.Model):
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES, default='other')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Credit(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    payment_category = models.CharField(max_length=100)  # e.g., Education, Medical, Housing
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class Debit(models.Model):
    mustahiq = models.ForeignKey(Mustahiq, on_delete=models.CASCADE)
    source = models.ForeignKey(Credit, on_delete=models.CASCADE)
    payment_category = models.CharField(max_length=100)  # e.g., Education, Medical, Housing
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
