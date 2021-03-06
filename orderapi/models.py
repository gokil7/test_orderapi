from django.db import models
from django.utils.timezone import now

class Order(models.Model):
    order_name = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    amount = models.IntegerField()
    cust_name = models.CharField(max_length=50)
    address = models.TextField()
    contact = models.CharField(max_length=70)

    def __str__(self):
        return self.order_name

class Contacted(models.Model):
    customerName = models.CharField(max_length=50)
    order = models.CharField(max_length=50)
    contacted = models.BooleanField()

    def __str__(self):
        return self.order
