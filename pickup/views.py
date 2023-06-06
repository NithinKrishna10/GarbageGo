# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PickupRequest
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
        print('==================================',request.data,"===============================")
        try:
            serializer = PickupRequestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print("Error",serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
