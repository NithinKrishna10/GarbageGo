from django.urls import path
from .views import WasteCategoryAPIView, WasteAPIView

urlpatterns = [
    path('waste-categories', WasteCategoryAPIView.as_view()),
    path('wastes', WasteAPIView.as_view()),
]
