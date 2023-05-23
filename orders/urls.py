from django.urls import path
from .views import PlaceOrderAPIView

urlpatterns = [
    path('place_order', PlaceOrderAPIView.as_view(), name='place-order'),
]
