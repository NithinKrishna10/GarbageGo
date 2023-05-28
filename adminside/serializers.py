from rest_framework.serializers import ModelSerializer
from accounts.models import User
from rest_framework import serializers
from services.models import Category,Waste
from orders.models import Order

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email','phone','is_active', 'password']
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
    fields = ['id', 'name', 'email','phone','is_active']








from waste.models import Waste,WasteCategory
from accounts.serializers import AddressSerializer
class WasteSerializer(ModelSerializer):
    class Meta:
        model = Waste
        fields = '__all__'


class WasteCategorySerializer(ModelSerializer):
    class Meta:
        model = WasteCategory
        fields = '__all__'
#  customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     waste_type = models.ForeignKey(WasteCategory,on_delete=models.CASCADE)
#     address = models.ForeignKey(Address,on_delete=models.CASCADE)
#     pickup_date = models.DateField()
#     additional_notes = models.TextField(blank=True)
#     is_ordered = models.BooleanField(default=False)
#     waste_weight = models.DecimalField(max_digits=10, decimal_places=2,default=0)
#     price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='Booked')
#     def __str__(self):
#         return f"Order #{self.pk} - {self.customer.name}"


class OrderSerializer(serializers.ModelSerializer):
    waste_type = WasteCategorySerializer()
    customer = UserSerializer()
    address = AddressSerializer()
    def get_waste_type_name(self, obj):
        return obj.waste_type.name
    
    def get_costomer_name(self,obj):
        return obj.customer.name
    
    def get_address(self,obj):
        return obj.address

    
    class Meta:
        model = Order
        fields = '__all__'