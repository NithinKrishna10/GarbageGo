from django.urls import path
from .views import ScrapAPIView

urlpatterns = [
    path('scrap-list', ScrapAPIView.as_view(), name='scrap-list'),
]
