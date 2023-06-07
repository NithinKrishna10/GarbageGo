from pickup.models import PickupRequest
from rest_framework.decorators import api_view
from .models import User
from rest_framework.response import Response
from django.db.models import Sum,Count
from datetime import datetime
current_date = datetime.now()

@api_view(['GET'])
def userdash(request,pk):
    # try:
    user = User.objects.get(id=pk) 
    # except User.DoesNotExist:
    #     raise Response("User not found.")

    try:
        user_pickups = PickupRequest.objects.filter(customer=user)
        user_total_weight = user_pickups.aggregate(user_total_weight=Sum('weight'))['user_total_weight']
    except:
        user_total_weight = 0
    # try:
    #     total_pickup_request = PickupRequest.objects.all()
    #     total_weight = total_pickup_request.aggregate(total_weight=Sum('weight'))['total_weight']
    # except Exception as e:
    #     return Response({'error': str(e)})


    # Get the total weight of monthly collected scrap
    try:
        scrap_weight = PickupRequest.objects.filter(
            customer = user,
            pickup_type='Scrap' ,
            pickup_month=current_date.month
        ).aggregate(total_weight=Sum('weight'))['total_weight'] or 0
    except:
        scrap_weight = 0
    # Get the total weight of monthly collected waste
    try:
        waste_weight = PickupRequest.objects.filter(
        customer = user,
        pickup_type='Waste',
        pickup_month=current_date.month
        ).aggregate(total_weight=Sum('weight'))['total_weight'] or 0
    except:
        waste_weight = 0
    # Calculate the total weight of monthly collected scrap and waste
    total_weight = scrap_weight + waste_weight

    print("Monthly Collected Scrap Weight:", scrap_weight)
    print("Monthly Collected Waste Weight:", waste_weight)
    print("Total Monthly Weight:", total_weight)

    payload = {
        'scrap_weight' :scrap_weight,
        'total_weight': total_weight,
        'user_total_weight': user_total_weight, 
        'waste_weight' : waste_weight,
        
    }
    return Response(payload)



@api_view(['GET'])
def monthly_pickup_count(request):
    monthly_data = PickupRequest.objects.values('pickup_month').annotate(count=Count('id'))
    return Response(list(monthly_data))

@api_view(['GET'])
def pickup_type_distribution(request):
    type_data = PickupRequest.objects.values('pickup_type').annotate(count=Count('id'))
    labels = [data['pickup_type'] for data in type_data]
    count = [data['count'] for data in type_data]
    return Response({'labels': labels, 'count': count})

@api_view(['GET'])
def daily_pickup_weight(request):
    daily_data = PickupRequest.objects.values('pickup_date').annotate(weight=Sum('weight'))
    labels = [data['pickup_date'].strftime('%Y-%m-%d') for data in daily_data]
    weight = [data['weight'] for data in daily_data]
    return Response({'labels': labels, 'weight': weight})

@api_view(['GET'])
def pickup_type_by_month(request):
    type_data = PickupRequest.objects.values('pickup_month', 'pickup_type').annotate(count=Count('id'))
    labels = sorted(list(set([data['pickup_month'] for data in type_data])))
    datasets = []
    for pickup_type in ['Waste', 'Scrap']:
        data = [data['count'] for data in type_data if data['pickup_type'] == pickup_type]
        datasets.append({'label': pickup_type, 'data': data})
    return Response({'labels': labels, 'datasets': datasets})


def pickup_weight_growth(request):
    data = PickupRequest.objects.values('pickup_month').annotate(total_weight=Sum('weight')).order_by('pickup_month')
    labels = [item['pickup_month'] for item in data]
    weights = [item['total_weight'] for item in data]
    response_data = {
        'labels': labels,
        'data': weights,
    }
    print(response_data,'=====================')
    return Response(response_data)