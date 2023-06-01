from .models import Scrap,ScrapCategory
from rest_framework.serializers import ModelSerializer

class ScrapCategorySerializer(ModelSerializer):
    class Meta:
        model = ScrapCategory
        fields = '__all__'

class ScrapSerializer(ModelSerializer):
    category = ScrapCategorySerializer()
    class Meta:
        model = Scrap
        fields = '__all__'

