from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from accounts.models import User
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from .serializers import WasteSerializer, WasteCategorySerializer
from waste.models import Waste, WasteCategory
from rest_framework.exceptions import APIException


class WasteCategoryView(APIView):

    def get(self, request):
        try:
            category = WasteCategory.objects.all()
            serializer = WasteCategorySerializer(category, many=True)
            return Response(serializer.data)
        except APIException as e:
            return Response(
                {'Waste_except': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        print('im here da')
        try:
            serializer = WasteCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response(
                {'waste_error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class WasteCategoryEdit(APIView):
    def get(self, request, pk):
        try:
            waste = WasteCategory.objects.get(id=pk)
            waste_serializer = WasteCategorySerializer(waste, many=False)
            return Response(waste_serializer.data)
        except WasteCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        print(pk, request.data)
        try:

            category = WasteCategory.objects.get(pk=pk)
        except WasteCategory.DoesNotExist:
            return Response({'error': 'WasteCategory not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WasteCategorySerializer(
            category, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors, "show the error")
        print(serializer.data,
              "djklsfklsdklfjlsdjflsdkfjlsfjlsdjflajsldj l jsd fjadisjfiosjdofj djffjiodj")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        wasteCat = WasteCategory.objects.get(id=pk)
        if not wasteCat:
            return Response(status=status.HTTP_404_NOT_FOUND)
        wasteCat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


api_view(['PATCH'])


class WasteListAPIView(APIView):
    def get(self, request):
        print('im here')
        try:
            waste = Waste.objects.all()
            serializer = WasteSerializer(waste, many=True)
            return Response(serializer.data)
        except APIException as e:
            return Response(
                {'waste_error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        print('im here')

        try:
            serializer = WasteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response(
                {'waste_error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['PATCH'])
def WasteEditAPIView(request, pk):
    try:
        scrap = Waste.objects.get(pk=pk)
        serializer = WasteSerializer(scrap, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except APIException as e:
        return Response(
            {'Waste_except': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )


class WasteEditView(APIView):
    def get(self, request, pk):
        print("this is pk", pk)
        try:
            wast = Waste.objects.get(id=pk)
            waste_serializer = WasteSerializer(wast, many=False)
            return Response(waste_serializer.data)
        except Waste.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        waste = Waste.objects.get(id=pk)
        if not waste:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WasteSerializer(waste, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors, "this is the fucking errors")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
