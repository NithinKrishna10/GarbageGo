from pickup.models import PickupRequest
from rest_framework.decorators import api_view
from .models import User
from rest_framework.response import Response
from django.db.models import Sum



@api_view(['GET'])
def userdash(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Response("User not found.")

    try:
        user_pickups = PickupRequest.objects.filter(customer=user)
        user_total_weight = user_pickups.aggregate(user_total_weight=Sum('weight'))['user_total_weight']
    except Exception as e:
        return Response({'error': str(e)})

    try:
        total_pickup_request = PickupRequest.objects.all()
        total_weight = total_pickup_request.aggregate(total_weight=Sum('weight'))['total_weight']
    except Exception as e:
        return Response({'error': str(e)})

    payload = {
        'total_weight': total_weight,
        'user_total_weight': user_total_weight,
    }

    return Response(payload)