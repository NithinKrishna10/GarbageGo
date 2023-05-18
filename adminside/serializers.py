from rest_framework.serializers import ModelSerializer
from accounts.models import User
from rest_framework import serializers
from services.models import Category,Scrap,Waste


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






from Scrap.models import Scrap ,ScrapCategory

class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = '__all__'


class ScrapCategorySerializer(ModelSerializer):
    class Meta:
        model = ScrapCategory
        fields = '__all__'