from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, AddressListAPIView, DistrictListAPIView, CityListAPIView, AddressPostAPIView, OrderListAPIView, CustomerPickupRequestAPIView
from .import views
from .import dashboard
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    # path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('addresses/<int:id>/', AddressListAPIView.as_view(), name='address-list'),
    path('addressess', AddressPostAPIView.as_view(), name='address-list'),

    path('verify_user', views.verify_token),
    path('districts', DistrictListAPIView.as_view(), name='district-list'),
    path('cities', CityListAPIView.as_view(), name='city-list'),
    path('orders/<int:pk>/', OrderListAPIView.as_view(), name='order-detail'),

    path('customer-pickup-requests/<int:customer_id>/',
         CustomerPickupRequestAPIView.as_view(), name='customer-pickup-requests'),


    #   Dash
    path('dash/<int:pk>/', dashboard.userdash, name="hai"),
    path('monthly_pickup_count/', dashboard.monthly_pickup_count, name='monthly_pickup_count'),
    path('pickup_type_distribution/', dashboard.pickup_type_distribution, name='pickup_type_distribution'),
    path('daily_pickup_weight/', dashboard.daily_pickup_weight, name='daily_pickup_weight'),
    path('pickup_type_by_month/', dashboard.pickup_type_by_month, name='pickup_type_by_month'),
    path('pickup_weight_growth/', dashboard.pickup_weight_growth, name='pickup_weight_growth'),

]
