from rest_framework import serializers
from .models import PickupRequest, Item


class PickupRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupRequest
        fields = '__all__'


class PickupItmeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
