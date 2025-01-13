from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address']

@admin.register(Mustahiq)
class MustahiqAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address']

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['donor', 'payment_category', 'amount', 'date']

@admin.register(Debit)
class DebitAdmin(admin.ModelAdmin):
    list_display = ['mustahiq', 'source', 'payment_category', 'amount', 'date']