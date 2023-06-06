# serializers.py
from rest_framework import serializers
from pickup.models import PickupRequest
from rest_framework.views import APIView

class PickupStatsSerializer(serializers.Serializer):
    monthly_pickups = serializers.IntegerField()
    daily_pickups = serializers.IntegerField()
    yearly_pickups = serializers.IntegerField()


# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

@api_view(['GET'])
def pickup_stats(request):
    if request.method == 'GET':
        current_date = datetime.now()
        monthly_pickups = PickupRequest.objects.filter(
            pickup_date__year=current_date.year,
            pickup_date__month=current_date.month
        ).count()

        daily_pickups = PickupRequest.objects.filter(
            pickup_date__year=current_date.year,
            pickup_date__month=current_date.month,
            pickup_date__day=current_date.day
        ).count()

        yearly_pickups = PickupRequest.objects.filter(
            pickup_date__year=current_date.year
        ).count()

        data = {
            'monthly_pickups': monthly_pickups,
            'daily_pickups': daily_pickups,
            'yearly_pickups': yearly_pickups,
        }

        serializer = PickupStatsSerializer(data)
        return Response(serializer.data)
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from django.db.models import Count
class YearlyPickupSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    count = serializers.IntegerField()
    
    
class PickupStatsView(APIView):
    def get(self, request, format=None):
        yearly_stats = PickupRequest.objects.values('pickup_month').annotate(count=Count('pk'))
        serialized_stats = YearlyPickupSerializer(yearly_stats, many=True)
        return Response(serialized_stats.data)
    
    
class DailyPickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupRequest
        fields = ('pickup_date', 'weight')
        
class DailyPickupListAPIView(ListAPIView):
    queryset = PickupRequest.objects.all()
    serializer_class = DailyPickupSerializer
    filterset_fields = ('pickup_date',)
    


@api_view(['GET'])
def monthly_pickup_data(request):
    monthly_data = PickupRequest.objects.values('pickup_month').annotate(count=Count('id'))
    return Response(list(monthly_data))