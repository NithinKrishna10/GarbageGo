from rest_framework import serializers
from .models import Order, OrderDetail

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['id', 'order', 'waste_weight', 'price', 'status']

class OrderSerializer(serializers.ModelSerializer):
    # order_detail = OrderDetailSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'waste_type', 'address', 'pickup_date', 'additional_notes']
