from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WasteCategory, Waste
from .serializers import WasteCategorySerializer, WasteSerializer

class WasteCategoryAPIView(APIView):
    def get(self, request):
        waste_categories = WasteCategory.objects.all()
        serializer = WasteCategorySerializer(waste_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WasteCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class WasteAPIView(APIView):
    def get(self, request):
        wastes = Waste.objects.all()
        serializer = WasteSerializer(wastes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WasteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
