from django.urls import path
from .views import PickupRequestListCreateAPIView

urlpatterns = [
    path('pickup-requests/', PickupRequestListCreateAPIView.as_view(), name='pickup_request_list_create'),
]
