from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer, OrderDetailSerializer
from .models import *


# class PlaceOrderAPIView(APIView):
#     def post(self, request):
#         print(request.data)
#         order_serializer = OrderSerializer(data=request.data)

#         order_detail_serializer = OrderDetailSerializer(data=request.data)

#         if order_serializer.is_valid() and order_detail_serializer.is_valid():
#             order = order_serializer.save()
#             order_detail_data = order_detail_serializer.validated_data
#             order_detail_data['order'] = order.id
#             order_detail = OrderDetail.objects.create(**order_detail_data)
      

#             return Response(
#                 {
#                     'order': order_serializer.data,
#                     'order_detail': order_detail_serializer.data
#                 },
#                 status=status.HTTP_201_CREATED
#             )
#         print(order_serializer.errors)
#         return Response(
#             {
#                 'order_errors': order_serializer.errors,
#                 'order_detail_errors': order_detail_serializer.errors
#             },
#             status=status.HTTP_400_BAD_REQUEST
#         )



class PlaceOrderAPIView(APIView):
    def post(self, request):
        order_serializer = OrderSerializer(data=request.data)

        if order_serializer.is_valid():
            order = order_serializer.save()
            print(order,'hjdfkhksdfhj')
            # order_details = OrderDetail()


            
            return Response(
                {
                    'order': order_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'order_errors': order_serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )