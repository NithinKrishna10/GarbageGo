from django.urls import path
from .views import PostView,PostDetailView

urlpatterns = [
    path('posts/', PostView.as_view(), name='post-list'),
     path('postsa/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # Add more URL patterns as needed
]
