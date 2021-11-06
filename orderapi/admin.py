from django.contrib import admin

from .models import Contacted, Order

admin.site.register(Order)
admin.site.register(Contacted)