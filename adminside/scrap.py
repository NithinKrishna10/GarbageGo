from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from accounts.models import User
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from .serializers import ScrapSerializer,ScrapCategorySerializer
from Scrap.models import Scrap,ScrapCategory



class ScrapCategoryView(APIView):

    def get(self,request):
        category = ScrapCategory.objects.all()
        serializer = ScrapCategorySerializer(category,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ScrapCategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScrapListAPIView(APIView):
    def get(self, request):
        scraps = Scrap.objects.all()
        serializer = ScrapSerializer(scraps, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ScrapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
def ScrapEditAPIView(request, pk):
    scrap = Scrap.objects.get(pk=pk)
    serializer = ScrapSerializer(scrap, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)