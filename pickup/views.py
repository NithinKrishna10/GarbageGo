# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PickupRequest,PickupTracker
from .serializers import PickupRequestSerializer


class PickupRequestListCreateAPIView(APIView):
    def get(self, request):
        try:
            pickup_requests = PickupRequest.objects.all()
            serializer = PickupRequestSerializer(pickup_requests, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = PickupRequestSerializer(data=request.data)
            if serializer.is_valid():
                pickup_request = serializer.save()

                # Update PickupTracker based on the pickup request
                user = pickup_request.customer
                pickup_type = pickup_request.pickup_type
                weight = pickup_request.weight

                pickup_tracker, _ = PickupTracker.objects.get_or_create(user=user)
                if pickup_type == 'Scrap':
                    pickup_tracker.scrap_weight += weight
                elif pickup_type == 'Waste':
                    pickup_tracker.waste_weight += weight
                pickup_tracker.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
