from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import * 
from .serializers import ScrapSerializer
# Create your views here.
class ScrapAPIView(APIView):
    def get(self, request):
        scraps = Scrap.objects.all()
        serializer = ScrapSerializer(scraps, many=True)
        return Response(serializer.data)
