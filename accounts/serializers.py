from rest_framework.serializers import ModelSerializer
from .models import User,Address,City,District

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email','phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        
        instance.save()
        return instance
    
class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']


class LoginDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email','phone']


class CitySerializer(ModelSerializer):
    class Meta:
        model=City
        fields ='__all__'
class DistrictSerializer(ModelSerializer):
    class Meta:
        model=District
        fields ='__all__'

class AddressSerializer(ModelSerializer):
    user = UserSerializer()
    district = DistrictSerializer()
    city =  CitySerializer()
    class Meta:
        model = Address
        fields = '__all__'

class AddressPostSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
