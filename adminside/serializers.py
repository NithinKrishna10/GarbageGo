from pickup.models import PickupRequest
from scrap.models import ScrapCategory, Scrap
from waste.models import Waste, WasteCategory
from accounts.serializers import AddressSerializer
from rest_framework.serializers import ModelSerializer
from accounts.models import User
from rest_framework import serializers

from orders.models import Order


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.is_superuser = True
        instance.save()
        return instance


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'is_active']


class WasteSerializer(ModelSerializer):
    class Meta:
        model = Waste
        fields = '__all__'


class WasteCategorySerializer(ModelSerializer):
    class Meta:
        model = WasteCategory
        fields = '__all__'


class ScrapCategorySerializer(ModelSerializer):
    class Meta:
        model = ScrapCategory
        fields = '__all__'


class ScrapSerializer(ModelSerializer):
    class Meta:
        model = Scrap
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    waste_type = WasteCategorySerializer()
    customer = UserSerializer()
    address = AddressSerializer()

    def get_waste_type_name(self, obj):
        return obj.waste_type.name

    def get_costomer_name(self, obj):
        return obj.customer.name

    def get_address(self, obj):
        return obj.address

    class Meta:
        model = Order
        fields = '__all__'


class PickupSerializer(serializers.ModelSerializer):

    customer = UserSerializer()
    pickup_address = AddressSerializer()

    def get_costomer_name(self, obj):
        return obj.customer.name

    def get_address(self, obj):
        return obj.address

    class Meta:
        model = PickupRequest
        fields = '__all__'

























































































