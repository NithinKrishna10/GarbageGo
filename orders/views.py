from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer, OrderDetailSerializer
from rest_framework.exceptions import APIException
from .models import *



    

class PlaceOrderAPIView(APIView):
    def post(self, request):
        try:
            order_serializer = OrderSerializer(data=request.data)
            order_serializer.is_valid(raise_exception=True)
            order = order_serializer.save()

            return Response(
                {
                    'order': order_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        except APIException as e:
            return Response(
                {
                    'order_errors': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
