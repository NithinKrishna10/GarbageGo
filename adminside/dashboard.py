# serializers.py
from rest_framework.generics import ListAPIView
from django.db.models import Sum, Count
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from pickup.models import PickupRequest
from rest_framework.views import APIView
from datetime import datetime
current_date = datetime.now()

class PickupStatsSerializer(serializers.Serializer):
    monthly_pickups = serializers.IntegerField()
    daily_pickups = serializers.IntegerField()
    yearly_pickups = serializers.IntegerField()


# views.py


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


class YearlyPickupSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    count = serializers.IntegerField()


class PickupStatsView(APIView):
    def get(self, request, format=None):
        yearly_stats = PickupRequest.objects.values(
            'pickup_month').annotate(count=Count('pk'))
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
    monthly_data = PickupRequest.objects.values(
        'pickup_month').annotate(count=Count('id'))
    return Response(list(monthly_data))


@api_view(['GET'])
def admindash(request):

    try:
        pickup_count = PickupRequest.objects.all().count()
    except:
        pickup_count=0
    
 
   
    
   
    
    try:
        scrap_weight = PickupRequest.objects.filter(
            pickup_type='Scrap',
            pickup_month=current_date.month
        ).aggregate(total_weight=Sum('weight'))['total_weight'] or 0
       
    except:
        scrap_weight = 0
        
    try:
        scrap_price = PickupRequest.objects.filter(
      
            pickup_type='Scrap',
            pickup_month=current_date.month
        ).aggregate(total_weight=Sum('price'))['total_weight'] or 0
        # print(scrap_price,"================================")
    except:
        scrap_price= 0
    # Get the total weight of monthly coll===============ected waste
    try:
        waste_weight = PickupRequest.objects.filter(

            pickup_type='Waste',
            pickup_month=current_date.month
        ).aggregate(total_weight=Sum('weight'))['total_weight'] or 0
    except:
        waste_weight = 0

    try:
        waste_price = PickupRequest.objects.filter(
      
            pickup_type='Waste',
            pickup_month=current_date.month
        ).aggregate(total_weight=Sum('weight'))['total_weight'] or 0
    except:
        waste_price = 0



    total_weight = scrap_weight + waste_weight

    print("Monthly Collected Scrap Weight:", scrap_weight)
    print("Monthly Collected Waste Weight:", waste_weight)
    print("Total Monthly Weight:", total_weight)

    payload = {
        'waste_price': waste_price,
        'scrap_price':scrap_price,
        'pickup_count' : pickup_count,
        'scrap_weight': scrap_weight,
        'total_weight': total_weight,
        'waste_weight': waste_weight,

    }

    return Response(payload)

