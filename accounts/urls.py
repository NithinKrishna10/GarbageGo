from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView,AddressListAPIView,DistrictListAPIView,CityListAPIView,AddressPostAPIView
from . import views
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    # path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('addresses/<int:id>/', AddressListAPIView.as_view(), name='address-list'),
    path('addressess', AddressPostAPIView.as_view(), name='address-list'),

    path('verify_user',views.verify_token),
    path('districts', DistrictListAPIView.as_view(), name='district-list'),
    path('cities', CityListAPIView.as_view(), name='city-list'),

]