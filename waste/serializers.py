from rest_framework import serializers
from .models import WasteCategory, Waste


class WasteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteCategory
        fields = '__all__'


class WasteSerializer(serializers.ModelSerializer):
    category = WasteCategorySerializer()

    class Meta:
        model = Waste
        fields = '__all__'
