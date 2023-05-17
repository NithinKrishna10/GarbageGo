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


class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'name', 'email','phone','is_active']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'images')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ScrapSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Scrap
        fields = ['id', 'name', 'category', 'description', 'weight', 'price', 'image']
        read_only_fields = ['id']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(id=category_data['id'])
        scrap = Scrap.objects.create(category=category, **validated_data)
        return scrap

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(id=category_data['id'])
        instance.name = validated_data.get('name', instance.name)
        instance.category = category
        instance.description = validated_data.get('description', instance.description)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
    


class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = ['id', 'name', 'category', 'description', 'weight', 'price', 'image']

