from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from accounts.models import User
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from .serializers import WasteSerializer,WasteCategorySerializer
from waste.models import Waste,WasteCategory

class WasteCategoryView(APIView):

    def get(self,request):
        category = WasteCategory.objects.all()
        serializer = WasteCategorySerializer(category,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WasteCategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WasteListAPIView(APIView):
    def get(self, request):
        waste = Waste.objects.all()
        serializer = WasteSerializer(waste, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = WasteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
@api_view(['PATCH'])
def WasteEditAPIView(request, pk):
    scrap = Waste.objects.get(pk=pk)
    serializer = WasteSerializer(scrap, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)