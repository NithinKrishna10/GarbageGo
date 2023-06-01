from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView,UserApi
from . import views
from . import scrap
from .orders import OrderDetailAPIView,OrderListAPIView
from .waste import WasteListAPIView,WasteCategoryView,WasteCategoryEdit,WasteEditView
from . import waste
from .scrap import *

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('userlist',views.userlist),
    path('logout', LogoutView.as_view()),
    path('userapi',UserApi.as_view()),
    path('block_user/<int:id>/', views.block_user, name='block_user'),
    path('unblock_user/<int:id>/', views.unblock_user, name='block_user'),
    path('addcat',views.category_list,name="addcat"),


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
]