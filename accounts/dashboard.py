from django.db.models import Sum, Count
from pickup.models import PickupRequest, PickupTracker
from rest_framework.decorators import api_view
from .models import User, Achievement
from rest_framework.response import Response
from django.db.models import Sum, Count
from .serializers import AchievementSerializer,PickupTrackerSerializer

from datetime import datetime
current_date = datetime.now()


@api_view(['GET'])
def userdash(request, pk):
    try:
        user = User.objects.get(id=pk)
        assign_achievements(user)
    except User.DoesNotExist:
        raise Response("User not found.")
    try:
        pickup_count = PickupRequest.objects.filter(customer=user).count()
    except:
        pickup_count=0
    try:
        user_pickups = PickupRequest.objects.filter(customer=user)

        user_total_weight = user_pickups.aggregate(user_total_weight=Sum('weight'))[
            'user_total_weight']
    except:
        user_total_weight = 0
 
    try:
        pickup_tracker = PickupTracker.objects.filter(user=user)
        
        pickup_tracker_serializer = PickupTrackerSerializer(pickup_tracker,many=True)
        serialized_pickup_tracker = pickup_tracker_serializer.data
        
        print(serialized_pickup_tracker,'====================')
    except:
    
        serialized_pickup_tracker = {

            'scrap_weight' : 0,
            'waste_weight' : 0,
        }
    
    try:
       achievement = Achievement.objects.filter(user=user)
       serializer = AchievementSerializer(achievement, many=True)
       serialized_achievements = serializer.data
    #    achievement = AchivementSerializer(data= achievements)
    except:
        achievement  = 'None'
    
    try:
        scrap_weight = PickupRequest.objects.filter(
            pickup_type='Scrap',
            pickup_month=current_date.month
        ).aggregate(total_weight=Sum('weight'))['total_weight'] or 0
       
    except:
        scrap_weight = 0
        
    try:
        scrap_price = PickupRequest.objects.filter(
            customer = user,
            pickup_type='Scrap',
            pickup_month=current_date.month
        ).aggregate(total_weight=Sum('price'))['total_weight'] or 0
        # print(scrap_price,"================================")
    except:
        scrap_price= 0

    try:
        waste_weight = PickupRequest.objects.filter(

            pickup_type='Waste',
            pickup_month=current_date.month
        ).aggregate(total_weight=Sum('weight'))['total_weight'] or 0
    except:
        waste_weight = 0

    try:
        waste_price = PickupRequest.objects.filter(
            customer = user,
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
        'achievement' : serialized_achievements,
        'pickup_tracker' : serialized_pickup_tracker,
        'scrap_weight': scrap_weight,
        'total_weight': total_weight,
        'user_total_weight': user_total_weight,
        'waste_weight': waste_weight,

    }

    return Response(payload)

















def assign_achievements(user):
    # Achievement 1: Pickup >= 50 kg of scrap
    total_scrap_weight = PickupTracker.objects.filter(user=user).aggregate(
        total_weight=Sum('scrap_weight'))['total_weight']
    if total_scrap_weight >= 50:
        Achievement.objects.get_or_create(
            user=user, name='Scrap Master', description='You have recycled more than 50 kg of scrap.', criteria='Recycle 50 kg of scrap')

    # Achievement 2: Pickup <= 50 kg of waste
    total_waste_weight = PickupTracker.objects.filter(user=user).aggregate(
        total_weight=Sum('waste_weight'))['total_weight']
    if total_waste_weight <= 50:
        Achievement.objects.get_or_create(
            user=user, name='Waste Warrior', description='You have recycled less than 50 kg of waste.', criteria='Recycle <= 50 kg of waste')

    # Achievement 3: Monthly 10 pickups booked
    monthly_pickup_count = PickupRequest.objects.filter(customer=user).annotate(
        pickup_count=Count('id')).filter(pickup_count__gte=10).exists()
    if monthly_pickup_count:
        Achievement.objects.get_or_create(user=user, name='Punctual Recycler',
                                          description='You have booked 10 or more pickups in a month.', criteria='Book 10 pickups in a month')




















@api_view(['GET'])
def monthly_pickup_count(request):
    monthly_data = PickupRequest.objects.values(
        'pickup_month').annotate(count=Count('id'))
    return Response(list(monthly_data))


@api_view(['GET'])
def pickup_type_distribution(request):
    type_data = PickupRequest.objects.values(
        'pickup_type').annotate(count=Count('id'))
    labels = [data['pickup_type'] for data in type_data]
    count = [data['count'] for data in type_data]
    return Response({'labels': labels, 'count': count})


@api_view(['GET'])
def daily_pickup_weight(request):
    daily_data = PickupRequest.objects.values(
        'pickup_date').annotate(weight=Sum('weight'))
    labels = [data['pickup_date'].strftime('%Y-%m-%d') for data in daily_data]
    weight = [data['weight'] for data in daily_data]
    return Response({'labels': labels, 'weight': weight})

@api_view(['GET'])
def pickup_type_by_month(request):
    type_data = PickupRequest.objects.values(
        'pickup_month', 'pickup_type').annotate(count=Count('id'))
    labels = sorted(list(set([data['pickup_month'] for data in type_data])))
    datasets = []
    for pickup_type in ['Waste', 'Scrap']:
        data = [data['count']
                for data in type_data if data['pickup_type'] == pickup_type]
        datasets.append({'label': pickup_type, 'data': data})
    return Response({'labels': labels, 'datasets': datasets})


def pickup_weight_growth(request):
    data = PickupRequest.objects.values('pickup_month').annotate(
        total_weight=Sum('weight')).order_by('pickup_month')
    labels = [item['pickup_month'] for item in data]
    weights = [item['total_weight'] for item in data]
    response_data = {
        'labels': labels,
        'data': weights,
    }
    print(response_data, '=====================')
    return Response(response_data)


