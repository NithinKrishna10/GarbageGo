from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pickup.models import PickupRequest, Item
from pickup.serializers import PickupRequestSerializer, PickupItmeSerializer
from .serializers import PickupSerializer
from drf_spectacular.utils import extend_schema
from .permissions import IsTokenVerified


class PickupRequestListCreateAPIView(APIView):
    permission_classes = [IsTokenVerified]
    extend_schema(responses=PickupItmeSerializer)

    def get(self, request):
        pickup_requests = PickupRequest.objects.all()
        serializer = PickupSerializer(pickup_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PickupRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PickupRequestRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsTokenVerified]
    def get_object(self, pk):
        try:
            return PickupRequest.objects.get(pk=pk)
        except PickupRequest.DoesNotExist:
            return None

    extend_schema(responses=PickupItmeSerializer)

    def get(self, request, pk):
        pickup_request = self.get_object(pk)
        if pickup_request:
            serializer = PickupRequestSerializer(pickup_request)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        pickup_request = self.get_object(pk)

        pickup_request.pickup_type = request.data['pickup_type']
        pickup_request.weight = request.data['weight']
        pickup_request.price = request.data['price']
        pickup_request.pickup_status = request.data['pickup_status']
        pickup_request.special_instructions = request.data['special_instructions']
        pickup_request.save()
        if 1 < 9:
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        pickup_request = self.get_object(pk)
        if pickup_request:
            pickup_request.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class PickupItemsView(APIView):
    permission_classes = [IsTokenVerified]
    extend_schema(responses=PickupItmeSerializer)

    def get(self, request):
        pickup_items = Item.objects.all()
        serializer = PickupItmeSerializer(pickup_items, many=True)

        return Response(serializer.data)
    extend_schema(request=PickupItmeSerializer, responses=PickupItmeSerializer)

    def post(self, request):

        serializer = PickupItmeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PickupDetailItemsView(APIView):
    permission_classes = [IsTokenVerified]
    extend_schema(responses=PickupItmeSerializer)
    def get(self, request, pk):
        pickup_items = Item.objects.filter(pickup_request=pk)
        serializer = PickupItmeSerializer(pickup_items, many=True)

        return Response(serializer.data)
