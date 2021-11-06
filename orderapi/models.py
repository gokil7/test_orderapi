from django.db import models
from django.utils.timezone import now

class Order(models.Model):
    order_name = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    amount = models.IntegerField()
    cust_name = models.CharField(max_length=50)
    address = models.TextField()
    contact = models.CharField()

    def __str__(self):
        return self.order_name
