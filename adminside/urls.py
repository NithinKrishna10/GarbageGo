from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView,UserApi
from . import views
from . import scrap
from .orders import OrderDetailAPIView,OrderListAPIView
from .waste import WasteListAPIView,WasteCategoryView,WasteCategoryEdit,WasteEditView
from . import waste
from .scrap import *

from .blog import PostDetailView,PostView,PostCategoryView,PostTagView
from .pickup import PickupRequestListCreateAPIView, PickupRequestRetrieveUpdateDestroyAPIView,PickupItemsView,PickupDetailItemsView
from . import dashboard
from .dashboard import PickupStatsView,DailyPickupListAPIView
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('verify_token',views.verify_token,name='verifytoken'),
    path('userlist',views.userlist),
    path('logout', LogoutView.as_view()),
    path('userapi',UserApi.as_view()),
    path('block_user/<int:id>/', views.block_user, name='block_user'),
    path('unblock_user/<int:id>/', views.unblock_user, name='block_user'),
  


    # path('scraps/<int:pk>/', ScrapRetrieveUpdateDestroyAPIView.as_view(), name='scrap-detail'),   
    # orders

    path('orders', OrderListAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('wastecategory',WasteCategoryView.as_view() ),
    path('wasteview',WasteListAPIView.as_view() ),

#  Waste Section

    path('waste-categories/', WasteCategoryView.as_view(), name='waste-category-list'),
    path('waste-edit/<int:pk>/', WasteCategoryEdit.as_view(), name='waste-edit'),
    path('waste-list/', WasteListAPIView.as_view(), name='waste-list'),
    path('waste-patch/<int:pk>/',WasteEditView.as_view(), name='waste-patch'),

# Scrap Section

    path('scrap-categories/', ScrapCategoryAPIView.as_view(), name='scrap-category-list'),
    path('scrap-categories/<int:pk>/', ScrapCategoryDetailAPIView.as_view(), name='scrap-category-detail'),
    path('scraps/', ScrapAPIView.as_view(), name='scrap-list'),
    path('scrapss/<int:pk>/', ScrapDetailAPIView.as_view(), name='scrap-detail'),

# Picku Section


    path('pickup-requests/', PickupRequestListCreateAPIView.as_view(), name='pickup_request_list_create'),
    path('pickup-request/<int:pk>/', PickupRequestRetrieveUpdateDestroyAPIView.as_view(), name='pickup_request_retrieve_update_destroy'),
    path('pickup-item',PickupItemsView.as_view(),name="pickup_items"),
    path('pickupitem/<int:pk>/',PickupDetailItemsView.as_view(),name="pickup_item"),
    
# Blog Section

    path('posts/', PostView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post-tags' , PostTagView.as_view(),name='tag' ),
    path('post-categories/',PostCategoryView.as_view(),name="post-category"),
    
    
# Dashboard
    path('dash',dashboard.admindash,name='ps'),
     path('pickup-stats/',PickupStatsView.as_view(), name='pickup-stats'),
       path('daily-pickups/', DailyPickupListAPIView.as_view(), name='daily-pickups'),
     path('monthly-pickups/', dashboard.monthly_pickup_data, name='monthly_pickups'),
]