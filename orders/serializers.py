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
    def da(self,validated_data):
        print(validated_data,'dfdfjklsdfjkdfjkldfjkl')
    # def create(self, validated_data):
    #     order_detail_data = validated_data.pop('order_detail')
    #     order = Order.objects.create(**validated_data)
    #     OrderDetail.objects.create(order=order, **order_detail_data)
    #     return order
