from rest_framework import serializers
# from rest_framework import
from .models import Contacted, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ContactedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacted
        fields = '__all__'