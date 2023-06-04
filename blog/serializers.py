from rest_framework import serializers
from .models import Post,Category,Tag
from accounts.serializers import UserSerializer
from accounts.models import User
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class PostSerializerr(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()
    # tags = TagSerializer()
    class Meta:
        model = Post
        fields = ['id','title', 'slug', 'author', 'category', 'tags', 'content', 'is_published', 'image','created_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'category', 'tags', 'content', 'is_published', 'image']

